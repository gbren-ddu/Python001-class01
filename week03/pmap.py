#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import logging
import socket
import IPy

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler)

def check_ip(ip_list):
    for ip in ip_list:
        result = os.popen(f'ping -c 1 -t 1 {ip}').read()
        if 'ttl' in result:
            print(f'{ip} 在线')
            # logger.info(f'{ip} 在线')
        else:
            print(f'{ip} 不在线')
            # logger.info(f'{ip} 不在线')

def check_port(ip, prot):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(3)
        res = s.connect_ex((ip, port))
        is_open = res == 0
    finally:
        s.close()
    if is_open:
        print(f'{ip}:{port} is listenning')
        # logger.info(f'{ip}:{port} is listenning')
    else:
        print(f'{ip}:{port} is not listenning')
        # logger.info(f'{ip}:{port} is not listenning')

def create_task(task_type, ip_list):
    if task_type == 'tcp':
        for ip in ip_list:
            for port in range(1, 1025):
                check_port(ip, port)
    else:
        for ip in ip_list:
            check_ip(ip)


if __name__ == "__main__":
    """
    -n：指定并发数量。
    -f ping：进行 ping 测试
    -f tcp：进行 tcp 端口开放、关闭测试。
    -ip：连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
    -w：扫描结果进行保存
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', choices=['ping', 'tcp'], dest='operation_type', default='tcp', help='protocol, ping or tcp')
    parser.add_argument('-ip', type=str, required=True, dest='ip_range', help='ip range, e.g. 192.168.1.1-192.168.1.128')
    parser.add_argument('-w', action='count', dest='saved_file', default=0, help='write to file')
    parser.add_argument('-v', action='count', dest='used_time', default=0, help='show elapsed time')

    group = parser.add_argument_group("concurrent")
    group.add_argument('-n', type=int, default=1, dest='worker_number', help='number of concurrent')
    group.add_argument('-m', choices=['proc', 'thread'], default='proc', dest='concurrent_type', help='multiprocess or threading', required=False)

    args = parser.parse_args()
    operation_type = args.operation_type
    ip_range = args.ip_range

    ip_list = IPy.IP(ip_range)
    create_task(operation_type, ip_list)



