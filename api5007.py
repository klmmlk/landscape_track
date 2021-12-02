#!/usr/bin/python
# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI, Body
from env import dtParms_User, dtParms_Group, superLevel

app = FastAPI()
login_json1 = superLevel.copy()
login_json1['dtParms_User'] = dtParms_User
login_json1['dtParms_Group'] = dtParms_Group
login_json2 = superLevel.copy()


@app.post('/api/User/UserLogin_New')
def UserLogin_New(data=Body(None)):
    """伪装登录用的"""
    login_json1['data']['userName'] = data['Mobile']
    login_json2['data']['userName'] = data['Mobile']
    # 包含可用命令信息
    if 'syncmode' in data:
        return login_json1
    # 不包含可用命令信息
    if 'PlatformId' in data and 'password' in data:
        return login_json2


@app.post('/api/CAD/CommandVipCheck')
def CommandVipCheck():
    """伪装命令检测用的"""
    return '2'


@app.post('/api/SystemConfig/GetUpdateRecored')
def GetUpdateRecored():
    """伪装命令检测用的"""
    return {"data": {"id": 23, "updatetime": "20211012",
                     "content": "\\n因服务器调整，自2021年10月18日开始，低于<2.71版>的景易CAD，将无法正常使用，烦请移步景易官网<手动下载>最新版安装下，不便之处，敬请谅解\\n(当前2.69版以上的，可直接在线升级.....)\\n\\n感谢您一如既往的支持，谢谢......",
                     "vision": "2.71"}, "state": 1, "info": "获取成功"}


@app.post('/api/Disk/ListDownloadInfo')
def ListDownloadInfo():
    """伪装命令检测用的"""
    return {"data": {"result": [
        {"downloadUrl": "", "fileSize": 0.0, "folderId": -1, "folderName": "景易CAD应用", "isFile": False,
         "createTime": None, "size": 0.0, "fileKey": None}], "isFree": True, "credit": 0.0}, "state": 1,
        "info": "获取成功!"}


@app.post('/api/CAD/GetCadAdver')
def GetCadAdver():
    """伪装命令检测用的"""
    return {"data": None, "state": 2, "info": "执行失败"}


if __name__ == '__main__':
    uvicorn.run(app, port=5007)
