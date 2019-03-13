#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,re
import sys
import json
import subprocess
import commands


# IP Info
def get_ip_info():
    ip_info = {}
    innerip_res = commands.getstatusoutput("ip a|grep inet|awk '{print $2}'|grep -E '^172|^192.168'")
    # for ipdb update, we will need the netmask ,so keep the netmask, ---later do it
    if innerip_res[0] == 0:
        innerips = innerip_res[1].split('\n')
        innerip_info = []
        if innerips:
            for i in innerips:
                innerip_info.append(i.split('/')[0])
        innerip_info.sort()
        ip_info['inner_ip'] = innerip_info
    else:
        ip_info['inner_ip'] = []
    guestip_res = commands.getstatusoutput( "ip a|grep inet|awk '{print $2}'|grep -E '^10\.'")

    if guestip_res[0] == 0:
        guestips = guestip_res[1].split('\n')
        guestip_info = []
        if guestips:
            for i in guestips:
                # 10.*.200~255.* or 10.255.*.* used by ucloud, others belongs to guest(do not record)
                ip_seg2 = i.split('/')[0].split('.')[1]
                ip_seg3 = i.split('/')[0].split('.')[2]
                if ip_seg2 == '255' or int(ip_seg3) > 191:
                    guestip_info.append(i.split('/')[0])
        guestip_info.sort()
        ip_info['guest_ip'] = guestip_info
    else:
        ip_info['guest_ip'] = []
    wanip_res = commands.getstatusoutput( "ip a|grep inet|awk '{print $2}'|grep -v -E '^172|^127|^10\.|^192.168|::'")
    if wanip_res[0] == 0:
        wanips = wanip_res[1].split('\n');
        wanip_info = []
        if wanips:
            for i in wanips:
                wanip_info.append(i.split('/')[0])
        wanip_info.sort()
        ip_info['wan_ip'] = wanip_info
    else:
            ip_info['wan_ip'] = []

    return ip_info


def get_hostname_info():
    hostname_res = commands.getstatusoutput('hostname')
    if hostname_res[0] == 0:
        return hostname_res[1].strip()
    else:
        return 'NotFound'


############# sys_infos_gathers #################
ksplice_cmd = '''updates=`lsmod | grep -E "^ksplice[^ ]*new" | cut -d ' ' -f 1`
if [ $? -ne 0 ]; then
    result="NULL"
    echo $result
    exit 0
fi
result=""
for update in $updates; do
    if [[ $result = "" ]]; then
        result=$update
    else
        result=${result}";"${update}
    fi
done
echo $result'''
############################ end of system info scripts #####################


def get_system_info():
    h = {}
    kernel_res = commands.getstatusoutput("uname -r")
    if kernel_res[0] == 0:
        kernel = kernel_res[1].strip()
    else:
        kernel = 'NotFound'

    os_res = commands.getstatusoutput("head -1 /etc/redhat-release")
    if os_res[0] == 0:
        os = os_res[1].strip()
    else:
        os = 'NotFound'

    cpu_res = commands.getstatusoutput("cat /proc/cpuinfo |grep processor |wc -l")
    if cpu_res[0] == 0:
        cpu = cpu_res[1].strip()
    else:
        cpu = 'NotFound'

    mem_res = commands.getstatusoutput("cat /proc/meminfo |grep MemTotal |awk -F ':' '{print $2}'")
    if mem_res[0] == 0:
        v_mem = mem_res[1].strip().split()[0]
        if v_mem:
            mem = str(int(v_mem)/1024000 + 1)+'G'  # 1024*1204
        else:
            mem = 'NotFound'
    else:
        mem = 'NotFound'

    disk_res = commands.getstatusoutput("df -h 2>/dev/null |grep vdb |awk '{print $2}'")
    if disk_res[0] == 0:
        disk = disk_res[1].strip()
    else:
        disk = 'NotFound'
    try:
        ksplice_res = subprocess.Popen(ksplice_cmd, shell=True, stdout=subprocess.PIPE)
        ksplice = ksplice_res.stdout.read().strip('\n')
    except:
        ksplice = 'NotFound'

    try:
        umon_res = commands.getstatusoutput("ps aux|grep -v grep |grep -c umonitor")
        umon_alive = int(umon_res[1])
        if umon_alive == 0:
            umonitor = 0
        else:
            umonitor = 1
    except:
        umonitor = 'NotFound'

    uuid_res = commands.getstatusoutput("dmidecode -t1|grep UUID|awk -F ': ' '{print $2}'|tr 'A-Z' 'a-z'")
    if uuid_res[0] == 0:
        uuid = uuid_res[1].strip()
    else:
        uuid = 'NotFound'

    h['kernel'] = kernel
    h['os']	= os
    h['cpu'] = cpu
    h['mem'] = mem
    h['disk'] = disk
    h['ksplice'] = ksplice
    h['uuid'] = uuid
    h['umonitor'] = umonitor

    return h


if __name__ == '__main__':
    realtime_info = {}
    try:
        hostname = get_hostname_info()
        realtime_info['hostname'] = hostname
    except Exception,e:
        realtime_info['hostanme'] = ''
        realtime_info['hostanme_errmesg'] = str(e)
    try:
        ip_info = get_ip_info()
        realtime_info['ipinfo'] = ip_info
        realtime_info['ipinfo_error'] = 0
    except Exception,e:
        realtime_info['ipinfo'] = {}
        realtime_info['ipinfo_error'] = 1
        realtime_info['ipinfo_errmesg'] = str(e)
    try:
        system_info = get_system_info()
        realtime_info['system'] = system_info
        realtime_info['system_error'] = 0
    except Exception,e:
        realtime_info['system'] = {}
        realtime_info['system_error'] = 1
        realtime_info['system_errmesg'] = str(e)

    outStr = json.dumps(realtime_info, ensure_ascii = False)

    print outStr
