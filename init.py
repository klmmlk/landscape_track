#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
import os
import re,shutil

host_window = r"C:\Windows\System32\drivers\etc\hosts"
host_mac = r"/etc/hosts"
HOST_LIVE = ["\n#LANDSCAPE",
             "127.0.0.1       www.landscape.ink"]
def backupHost():
    hostsBack = r'C:\Windows\system32\drivers\etc\hosts.bak'
    if os.path.lexists(hostsBack) == False:
        shutil.copy(host_window, hostsBack)

def search_host(hostvalue, host_path):
    hostfile = open(host_path, 'r')
    each_line = hostfile.readlines()
    hostfile.close()
    findresult = re.findall(hostvalue, ''.join(each_line))
    return findresult


def write_host(hostvalue):
    if os.name == "nt":
        output = open(host_window, 'a')
    else:
        output = open(host_mac, 'a')

    for insid in hostvalue:
        output.write(insid)
        output.write("\n")
    output.close()

if __name__ == '__main__':
    if search_host(HOST_LIVE[0],host_window):
        print("it exist, no need to update")
    else:
        write_host(HOST_LIVE)