#!/usr/bin/env bash

path=$1

for ip in $(cat $path)
do
    scp ./sdk-gateway.tar.gz root@$ip:/root/

done