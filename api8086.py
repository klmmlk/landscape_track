#!/usr/bin/python
# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI
from env import vedioList

app = FastAPI()


@app.api_route('/api/Course/GetLessonVedioList/',methods=['GET','POST'])
def list():
    """伪装登录用的"""
    return vedioList

if __name__ == '__main__':
    uvicorn.run(app,port=8086)