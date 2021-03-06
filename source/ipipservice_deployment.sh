#!/usr/bin/env bash

set -e

filepath=$1
for ip in $(cat $filepath)
do
    echo '>>>deploying host:' $ip

    echo '>>>scp ipipservice.tar.gz file to host:' $ip
    scp ./ipipservice.tar.gz root@$ip:/root/

    echo '>>>scp meld3 to host:' $ip
    scp ./meld3-1.0.2-py2.py3-none-any.whl root@$ip:/root/

    echo '>>>scp supervisor.tar.gz to host:' $ip
    scp ./supervisor-3.3.5.tar.gz root@$ip:/root/

    echo '>>>scp supervisor.conf to host:' $ip
    scp ./supervisord.conf root@$ip:/root/


    ssh -l root $ip "

        mkdir -p /opt/supervisor/
        mv /root/meld3-1.0.2-py2.py3-none-any.whl /root/supervisor-3.3.5.tar.gz /opt/supervisor/
        cd /opt/supervisor/
        tar -zxvf supervisor-3.3.5.tar.gz
        pip install meld3-1.0.2-py2.py3-none-any.whl
        cd supervisor-3.3.5 && python setup.py install

        mkdir -p /etc/supervisor/conf.d
        mv /root/supervisord.conf /etc/supervisor/

        mkdir -p /data/sdk-gateway
        mv /root/ipipservice.tar.gz /data/sdk-gateway/
        cd /data/sdk-gateway/
        tar -zxvf ipipservice.tar.gz

        supervisord -c /etc/supervisor/supervisord.conf
    "
done

