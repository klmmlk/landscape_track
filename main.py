#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
import threading
import api5007,api8008,api8086,uvicorn

def run5007():
    uvicorn.run(api5007.app, port=5007)

def run8008():
    uvicorn.run(api8008.app, port=8008)

def run8086():
    uvicorn.run(api8086.app, port=8086)

if __name__ == '__main__':
    t1 = threading.Thread(target=run5007)
    t2 = threading.Thread(target=run8008)
    t3 = threading.Thread(target=run8086)
    t1.start()
    t2.start()
    t3.start()