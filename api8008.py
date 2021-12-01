#!/usr/bin/python
# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
app = FastAPI()


@app.post('/api/CloudDisk/CloudDiskSizeInfo')
def CloudDiskSizeInfo():
    """伪装命令检测用的"""
    return JSONResponse(status_code=404)

@app.post('/api/CloudDisk/ListCloudDisk')
def ListCloudDisk():
    """伪装命令检测用的"""
    return JSONResponse(status_code=404)

@app.post('/api/CloudDisk/GetJYAppFolderid')
def GetJYAppFolderid():
    """伪装命令检测用的"""
    return JSONResponse(status_code=404)

if __name__ == '__main__':
    uvicorn.run(app, port=8008)
