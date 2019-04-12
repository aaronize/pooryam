#!/usr/bin/env python
# encoding=utf8

import requests
import time
import sys
import re
import shutil
import hashlib
import multiprocessing as mp
import subprocess as sp


def download_ipdb(url, path):
    response = requests.get(url, verify=False)
    etag_value = response.headers.get("ETag")
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # ETag不存在就退出
    if not etag_value:
        print current_time, " etag not exists"
        return False

    # 写临时文件
    with open(path + "/ipip_temp.ipdb", 'wb+') as fd:
        for chunk in response.iter_content(4096):
            fd.write(chunk)

    # 读取临时文件
    with open(path + "/ipip_temp.ipdb", 'rb') as fd:
        sha1 = hashlib.sha1()
        while True:
            content = fd.read(4096)
            if not content:
                break
            sha1.update(content)

        # 计算临时文件sha1
        content_sha1_value = sha1.hexdigest()
        etag_sha1_value = etag_value[5:]
        # sha1 不一致退出
        if etag_sha1_value != content_sha1_value:
            print current_time, " etag err"
            return False

    # 覆盖正式文件，目标目录必须有可写权限。
    shutil.copyfile(path + "/ipip_temp.ipdb", path + "/ipip.ipdb")
    print current_time, " download ok"
    return True


def dispatch_ipdb(path, ip_list):
    output = list()
    ret_set = list()
    pool = mp.Pool()
    for ip in ip_list:
        ret_set.append(pool.apply_async(func=scp_file, args=(ip, path)))

    pool.close()
    pool.join()

    for ret in ret_set:
        output.append(ret.get())

    return output


def scp_file(ip, path):
    cmd = '/usr/bin/scp {} root@{}:/data/'.format(path, ip)
    proc = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    try:
        proc.wait()
        err_msg = proc.stderr.read().decode('utf-8')
    except Exception, e:
        err_msg = str(e)

    if proc.poll() is not None and re.search('Connection refused|No route to host|Permission denied|'
                                             'Network is unreachable|Host key verification failed', err_msg) is None:
        info = {'result': 'success', 'info': ''}
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), ' scp文件至{}成功'.format(ip)
    else:
        info = {'result': 'failed', 'info': err_msg}
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), ' scp文件至{}失败, {}'.format(ip, err_msg)

    return info


if __name__ == "__main__":
    iplist_path = sys.argv[1]

    down_url = "https://user.ipip.net/download.php?type=ipdb&token=TOKEN"
    down_path = "/root/sdk_related_deploy/ipdb"

    ipdb_path = down_path + "/ipip.ipdb"
    host_list = list()

    for line in open(iplist_path):
        tmp = line.strip()
        if tmp != '' and not tmp.startswith('#'):
            host_list.append(tmp)

    if not download_ipdb(down_url, down_path):
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), " 下载文件失败，没有执行文件分发"
    else:
        dispatch_ipdb(ipdb_path, host_list)
