# showTxcjm('****************');return false;
# -> /archive/gdjy/txcjm/show.action?id=****************
# <- {"result":{"finished":true,"logId":"----------------","archiveId":"****************","taskId":""},"message":"","status":0}

# -> /archive/gdjy/txcjm/pic.action?logId=----------------
# -> /archive/gdjy/txcjm/download.action?logId=----------------


import base64
import json
from datetime import datetime

from PIL import Image
from pyzbar import pyzbar


def decode_qr_code(image_path):
    img = Image.open(image_path)
    result = pyzbar.decode(img)
    return result[0].data.decode("utf-8")


def decode(cjm, encoding="utf-8"):
    s = base64.b64decode(cjm).decode(encoding)
    j = json.loads(s)
    return j


def pretty_print(info):
    ts = int(info["sjc"]) / 1000  # 转为秒
    dt = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    info["sjc"] = f'{info["sjc"]} ({dt})'

    keys = {
        "sjc": "时间戳",  #
        "cjm": "采集码",
        "yxdm": "院校代码",  # 西北大学10697
        "zjhm": "证件号码",  # 身份证后4位
        "xh": "学号",
        "cc": "层次",  # 本科
        "xllb": "学历类别",  # 普通
        "fy": "分院",  # XX学院
        "xm": "姓名",
        "bh": "班号",  #
    }
    for k in keys:
        print(f"{keys[k]:<6}\t{info[k]}")


cjm = decode_qr_code("采集码.png")
info = decode(cjm)
pretty_print(info)
