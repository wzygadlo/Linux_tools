#!/usr/bin/env python
# Python version 3.5

import re
import subprocess
import itertools
import collections


def find_ip_address():
    '''Searching for ip address in log file '''
    raw_data = open('/var/log/auth.log')
    logs = raw_data.read()
    raw_data.close()
    loglist = logs.splitlines()
    ip_addr = []
    ip = []
    for index, message in enumerate(loglist):
        if 'Failed password' in message:
            ip_addr.append(re.findall(r'\b[0-9]+(?:\.[0-9]+){3}\b', message))
    uniq_ip = collections.Counter((list(itertools.chain(*ip_addr))))
    for key, value in uniq_ip.items():
        if int(value) > 4:
            ip.append(key)
    return ip


def add_iptable_rules():
    ip_addr = find_ip_address()
    for ip in ip_addr:
        if ip not in subprocess.getoutput('sudo iptables -L -n'):
            subprocess.getoutput('sudo iptables -I INPUT -s {} -j DROP'.format(ip))

if __name__ == "__main__":
    add_iptable_rules()
