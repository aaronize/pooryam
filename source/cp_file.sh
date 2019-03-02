#!/usr/bin/env bash

path=$1

for ip in $(cat $path)
do
    echo 'scp config.json to host:' $ip
    scp ./config.json root@$ip:/opt/sdk-gateway/conf/

    ssh -l root $ip "supervisorctl restart sdk-gateway"
done