#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

# pyinstaller -F -w main.py -p api5007.py -p api8008.py -p api8086.py -p init.py
import threading,time
import api5007,api8008,api8086,uvicorn
import init

def run5007():
    uvicorn.run(api5007.app, port=5007)

def run8008():
    uvicorn.run(api8008.app, port=8008)

def run8086():
    uvicorn.run(api8086.app, port=8086)

if __name__ == '__main__':
    # 限制使用时间
    # if int(time.time()) >= 1639123955:
    #     exit(0)
    # 备份修改hosts
    init.backupHost()
    if init.search_host(init.HOST_LIVE[0],init.host_window):
        print("it exist, no need to update")
    else:
        init.write_host(init.HOST_LIVE)

    t1 = threading.Thread(target=run5007)
    t2 = threading.Thread(target=run8008)
    t3 = threading.Thread(target=run8086)
    t1.start()
    t2.start()
    t3.start()