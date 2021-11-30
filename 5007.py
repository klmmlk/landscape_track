#!/usr/bin/python
# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI, Body

app = FastAPI()
login_json1 = {"data": {"userId": 3549, "userName": "klmmlk", "openid": None, "mobile": "18628281629",
                        "avatar": "http://landscape-public.oss-cn-hangzhou.aliyuncs.com/00%20LandscapeInkApp/Files/bf0e02f5-0872-4918-989b-d61e71c3cf87.png",
                        "nickname": "解药", "powerid": 2, "money": 0.00, "credit": 3388.80, "duedate": "2099-03-15",
                        "duedate_Cadyuanjian": "0", "duedate_Cadlvzhi": "0", "pptDuetime": "2020-01-15",
                        "psDuetime": None, "group": "", "pptGroup": "2019-12-11", "psGroup": None, "sub": "Client",
                        "tokenType": "Web",
                        "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VyTmFtZSI6ImtsbW1sayIsIlVzZXJJZCI6IjM1NDkiLCJNb2JpbGUiOiIxODYyODI4MTYyOSIsImlhdCI6IjIwMjEvMTEvMzAgMTU6NDc6MjciLCJleHAiOjE2NDA4NzkyNDcsImlzcyI6ImxhbmRzY2FwZWluayIsImF1ZCI6IjYwMDMyNTMifQ.281RytfbRo5OZ5vbsX-Qa_cn6Wo4QEynUj4WwQqNXEo",
                        "authCode": "fk8UZ4", "dtParms_User": [
        {"id": 21360, "name": "上木", "type": "LAYER", "value": "03LS-上木|80.0", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21361, "name": "中层", "type": "LAYER", "value": "03LS-中层|80.0", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21362, "name": "景观设计线", "type": "LAYER", "value": "01LS-景观设计线|33", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21363, "name": "道路中心线", "type": "LAYER", "value": "01LS-道路中心线|1", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21364, "name": "轴线", "type": "LAYER", "value": "01LS-轴线|1", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21365, "name": "等高线", "type": "LAYER", "value": "03LS-绿化地形|11", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21366, "name": "等高值", "type": "LAYER", "value": "03LS-绿化地形注释|7", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21367, "name": "临时填充", "type": "LAYER", "value": "01LS-临时填充|251", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21368, "name": "地被填充", "type": "LAYER", "value": "03LS-地被填充|8", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21369, "name": "铺装分割", "type": "LAYER", "value": "01LS-铺装分割|144", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21370, "name": "铺装填充", "type": "LAYER", "value": "01LS-铺装填充|252", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21371, "name": "上木标注", "type": "LAYER", "value": "03LS-上木标注|50", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21372, "name": "中层标注", "type": "LAYER", "value": "03LS-中层标注|50", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21373, "name": "地被线", "type": "LAYER", "value": "03LS-地被线|60", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21374, "name": "地被标注", "type": "LAYER", "value": "03LS-地被标注|70", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21375, "name": "临时变色", "type": "LAYER", "value": "03LS-临时变色|251", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21376, "name": "尺寸", "type": "LAYER", "value": "02LS-尺寸|3", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21377, "name": "标注", "type": "LAYER", "value": "02LS-标注|3", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21378, "name": "坐标", "type": "LAYER", "value": "02LS-坐标|3", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21379, "name": "竖向", "type": "LAYER", "value": "02LS-竖向|3", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21380, "name": "图名与索引", "type": "LAYER", "value": "02LS-图名与索引|1", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21381, "name": "图框", "type": "LAYER", "value": "02LS-图框|123", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21382, "name": "电气图块", "type": "LAYER", "value": "05LS-电气图块|34", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21383, "name": "电气线缆", "type": "LAYER", "value": "05LS-电气线缆|122", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21384, "name": "给水图块", "type": "LAYER", "value": "05LS-给水图块|34", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21385, "name": "给水线缆", "type": "LAYER", "value": "05LS-给水线缆|122", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21386, "name": "排水图块", "type": "LAYER", "value": "05LS-排水图块|164", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21387, "name": "排水线缆", "type": "LAYER", "value": "05LS-排水线缆|183", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21388, "name": "配景", "type": "LAYER", "value": "01LS-配景|54", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21389, "name": "网格线", "type": "LAYER", "value": "02LS-网格线|160", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 21390, "name": "TXTSTYLE", "type": None, "value": "LS_TEXT|tssdeng|hztxt|0.8|3", "remarks": None,
         "userName": "klmmlk", "userId": None},
        {"id": 21391, "name": "TITLE_TXTSTYLE", "type": None, "value": "LS_TITLE|黑体||1|5", "remarks": None,
         "userName": "klmmlk", "userId": None},
        {"id": 21392, "name": "上木箭头", "type": None, "value": "圆点", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 27847, "name": "绘图单位", "type": None, "value": "M", "remarks": None, "userName": "klmmlk",
         "userId": None},
        {"id": 31417, "name": "收边参数", "type": None, "value": "300@300|300@300*2|300@300+150@150|300@300+150@150_P",
         "remarks": None, "userName": "klmmlk", "userId": None},
        {"id": 34311, "name": "字高列表", "type": None, "value": "0.8,1.2,1.5,1.8,2.24,2.4,2.6,3,3.37,3.5,5,7,10,14",
         "remarks": None, "userName": "klmmlk", "userId": 0},
        {"id": 34312, "name": "启用中层标注", "type": None, "value": "1", "remarks": None, "userName": "klmmlk", "userId": 0},
        {"id": 34313, "name": "绿植标注点大小", "type": None, "value": "2.0", "remarks": None, "userName": "klmmlk",
         "userId": 0}], "dtParms_Group": [
        {"id": 32164, "name": "上木", "type": "LAYER", "value": "03LS-上木|80.0", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32165, "name": "中层", "type": "LAYER", "value": "03LS-中层|80.0", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32166, "name": "景观设计线", "type": "LAYER", "value": "01LS-景观设计线|33", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32167, "name": "道路中心线", "type": "LAYER", "value": "01LS-道路中心线|1", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32168, "name": "轴线", "type": "LAYER", "value": "01LS-轴线|1", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32169, "name": "等高线", "type": "LAYER", "value": "03LS-绿化地形|11", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32170, "name": "等高值", "type": "LAYER", "value": "03LS-绿化地形注释|7", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32171, "name": "临时填充", "type": "LAYER", "value": "01LS-临时填充|251", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32172, "name": "地被填充", "type": "LAYER", "value": "03LS-地被填充|8", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32173, "name": "铺装分割", "type": "LAYER", "value": "01LS-铺装分割|144", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32174, "name": "铺装填充", "type": "LAYER", "value": "01LS-铺装填充|252", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32175, "name": "上木标注", "type": "LAYER", "value": "03LS-上木标注|50", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32176, "name": "中层标注", "type": "LAYER", "value": "03LS-中层标注|50", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32177, "name": "地被线", "type": "LAYER", "value": "03LS-地被线|60", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32178, "name": "地被标注", "type": "LAYER", "value": "03LS-地被标注|70", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32179, "name": "临时变色", "type": "LAYER", "value": "03LS-临时变色|251", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32180, "name": "尺寸", "type": "LAYER", "value": "02LS-尺寸|3", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32181, "name": "标注", "type": "LAYER", "value": "02LS-标注|3", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32182, "name": "坐标", "type": "LAYER", "value": "02LS-坐标|3", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32183, "name": "竖向", "type": "LAYER", "value": "02LS-竖向|3", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32184, "name": "图名与索引", "type": "LAYER", "value": "02LS-图名与索引|1", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32185, "name": "图框", "type": "LAYER", "value": "02LS-图框|123", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32186, "name": "电气图块", "type": "LAYER", "value": "05LS-电气图块|34", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32187, "name": "电气线缆", "type": "LAYER", "value": "05LS-电气线缆|122", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32188, "name": "给水图块", "type": "LAYER", "value": "05LS-给水图块|34", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32189, "name": "给水线缆", "type": "LAYER", "value": "05LS-给水线缆|122", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32190, "name": "排水图块", "type": "LAYER", "value": "05LS-排水图块|164", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32191, "name": "排水线缆", "type": "LAYER", "value": "05LS-排水线缆|183", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32192, "name": "配景", "type": "LAYER", "value": "01LS-配景|54", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32193, "name": "网格线", "type": "LAYER", "value": "02LS-网格线|160", "remarks": None, "userName": "",
         "userId": 0},
        {"id": 32194, "name": "TXTSTYLE", "type": None, "value": "LS_TEXT|tssdeng|ntst|0.8|3", "remarks": None,
         "userName": "", "userId": 0},
        {"id": 32195, "name": "TITLE_TXTSTYLE", "type": None, "value": "LS_TITLE|黑体||1|5", "remarks": None,
         "userName": "", "userId": 0},
        {"id": 32196, "name": "字高列表", "type": None, "value": "0.8,1.2,1.5,1.8,2.24,2.4,2.6,3,3.37,3.5,5,7,10,14",
         "remarks": None, "userName": "", "userId": 0},
        {"id": 32197, "name": "上木箭头", "type": None, "value": "圆点", "remarks": None, "userName": "", "userId": 0},
        {"id": 90018, "name": "上木图例模式", "type": None, "value": "1", "remarks": None, "userName": "", "userId": 0},
        {"id": 91497, "name": "快切图层", "type": None, "value": "0=ee|01LS-景观设计线=rr|01LS-建构筑物=tt", "remarks": None,
         "userName": "", "userId": 0}], "localUsed": True, "removeUsed": False, "password": None, "isSupplier": False,
                        "imUserSig": "eJwtjEELgjAYQP-Ldw6Zc5tz0ME06qChZWLdAmd8iDGWSBH998R2fO-B*0CVnbxJW1BAPQKrhbHVjxE7XLQIOItceLb9zRhsQfmMEM5EJMm-6JdBq0EJwiRxbsRhNr4IJJUhZaF74H2*ZmWSiGu5p6nmRT8127FgttoMh-hYmy7O3*eori5Bmu-KNXx-Q0UvUQ__"},
               "state": 1, "info": "Vip-20990315&20211130"}
login_json2 = {
    "data": {
        "userId": 3549,
        "userName": "klmmlk",
        "openid": None,
        "mobile": "18628281629",
        "avatar": "http://landscape-public.oss-cn-hangzhou.aliyuncs.com/00%20LandscapeInkApp/Files/bf0e02f5-0872-4918-989b-d61e71c3cf87.png",
        "nickname": "解药",
        "powerid": 2,
        "money": 0,
        "credit": 3388.8,
        "duedate": "2099-03-15",
        "duedate_Cadyuanjian": "0",
        "duedate_Cadlvzhi": "0",
        "pptDuetime": "2020-01-15",
        "psDuetime": None,
        "group": "",
        "pptGroup": "2019-12-11",
        "psGroup": None,
        "sub": "Client",
        "tokenType": "Web",
        "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VyTmFtZSI6ImtsbW1sayIsIlVzZXJJZCI6IjM1NDkiLCJNb2JpbGUiOiIxODYyODI4MTYyOSIsImlhdCI6IjIwMjEvMTEvMzAgMjowMDowMCIsImV4cCI6MTY0MDgyOTYwMCwiaXNzIjoibGFuZHNjYXBlaW5rIiwiYXVkIjoiNjAwMzI1MyJ9.C9cTBxusIUucRK3YYK9hUIbuVdHrgQPjoj7zO2wIPIM",
        "authCode": "fk8UZ4",
        "dtParms_User": [],
        "dtParms_Group": [],
        "localUsed": True,
        "removeUsed": False,
        "password": None,
        "isSupplier": False,
        "imUserSig": "eJyrVgrxCdYrSy1SslIy0jNQ0gHzM1NS80oy0zLBwmbGpiaWUInilOzEgoLMFCUrQxMDA1MTM0sLA4hMakVBZlGqkpWZgYmFAVSsJDMXKGJoZmxhZGxuBhMtzkwHmurnUZrumlFi5hdSGpXsEhyaHljilOqVVJWhnWKYlxOWn2fm5mecbuFSYZltq1QLAGRfMGA_"
    },
    "state": 1,
    "info": "Vip-20990315&20211130"
}

command_check = {'name': 'klmmlk', 'cpuid': 'KINGSTONSNVS500GBFEBFBFF000906EA', 'type': '2'}


@app.post('/api/User/UserLogin_New')
def login(data=Body(None)):
    """伪装登录用的"""
    if 'syncmode' in data:
        return login_json1
    if 'PlatformId' in data and 'password' in data:
        return login_json2


@app.post('/api/CAD/CommandVipCheck')
def vipCheck():
    """伪装命令检测用的"""
    return command_check


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
