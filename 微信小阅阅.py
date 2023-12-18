"""
cron: 0 0  7-23 * * *
new Env('微信小阅阅')

随便写，不确定能用
打开https://wi.yfinfo.top:10251/yunonline/v1/auth/7ebab1ff1190208e60a290f08646cd46?codeurl=wi.yfinfo.top:10251&codeuserid=2&time=1696138373

查下面ck参数 ysmuidm，填入ysmuidList内

by dunkuenfai

"""

import requests
import time
import json
import re
from urllib import parse
import random


ysmuidList = [
    "29a3867bb367ca26196405d8*bcea04d",
    "0d17ad03e98ecb56ea79f4b09e9a***",
    "e78214c19490440d7902d085**3e404*",
    "40bda2e5ef6839a5f48f36a**e6db5a3",
    "1f07065ea0c7a7102e344ee1bd0*d187",
]

# ysmuid = "29a3867bb367ca26196405d8ebcea04d"
# unionid = "oZdBp05So3-mR3-0TQwJgvAo3iGw"


uk = ""
unionid = ""
ysmuid = ""


def getDomain():
    url = "http://1695977764.szcoin.site/yunonline/v1/wtmpdomain"

    payload = "unionid=" + unionid
    headers = {
        "Host": "1695977764.szcoin.site",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://1695977764.szcoin.site",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a28) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "http://1695977764.szcoin.site/?cate=0",
        "Content-Length": "36",
        "Cookie": "ejectCode=1; ysmuid=" + ysmuid,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = json.loads(response.text)
    #   data=json.loads(data)
    #   link=(data['data']['domain'])
    #   n=link.find('uk')
    #   link=link[n+3:n+35]
    #   print('link',link)
    return data


def cate():  # 获取首页提现链接
    url = "http://1696031853.szcoin.site/?cate=0"
    payload = {}
    headers = {
        "Host": "1696006141.tyjnwb.top",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Cookie": "ysmuid=" + ysmuid,
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a28) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    getUnionid = re.findall(r'// var unionid="(.*)"', response.text)
    print(getUnionid)
    data = re.findall(r'href="(.*)">提现', response.text)
    data = parse.urlparse(data[0])
    data = parse.parse_qs(data.query)
    data["uid"] = getUnionid

    return data


def remain():
    url = "http://1696031853.szcoin.site/yunonline/v1/gold?unionid=" + unionid

    payload = {}
    headers = {
        "Host": "1696031853.szcoin.site",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "ejectCode=1; ysmuid=" + ysmuid,
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a28) NetType/WIFI Language/zh_CN",
        "Referer": "http://1696031853.szcoin.site/?cate=0",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "X-Requested-With": "XMLHttpRequest",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)
    return data


def user_gold():  # 金币兑换现金
    last_gold = remain()["data"]["last_gold"]
    if int(last_gold) < 3000:
        print("剩余金币少于3000，不能提现！")
        return
    gold = str(int(int(last_gold) / 1000) * 1000)
    urlparad = cate()
    print(urlparad)
    url = "http://1696125063.szcoin.site/yunonline/v1/user_gold"
    payload = (
        "unionid="
        + urlparad["unionid"][0]
        + "&request_id="
        + urlparad["request_id"][0]
        + "&gold="
        + gold
    )
    headers = {
        "Host": "1696125063.szcoin.site",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://1696125063.szcoin.site",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a28) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "http://1696125063.szcoin.site/yunonline/v1/exchange?unionid=d81eed515140b58793bb86fcc380610a&request_id=e3427d819d275f5ee807546bd08a34cc&qrcode_number=16934700709359033&addtime=1695969519",
        "Content-Length": "96",
        "Cookie": "ysmuid=" + ysmuid,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def withdraw(arg):
    url = "http://1695979173.szcoin.site/yunonline/v1/withdraw"

    payload = (
        "unionid="
        + arg["unionid"][0]
        + "&signid="
        + arg["request_id"][0]
        + "&ua=1&ptype=0&paccount=&pname="
    )
    headers = {
        "Host": "1695979173.szcoin.site",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://1695979173.szcoin.site",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a28) NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "http://1695979173.szcoin.site/yunonline/v1/exchange?unionid=1846c01eab33acc830b37d071c7bf933&request_id=e5f2107157c1c2ef05a7d417ffd218a4&qrcode_number=16934700709359033&addtime=1695969519",
        "Content-Length": "112",
        "Cookie": "ysmuid=" + ysmuid,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def step1():
    url = "http://1696006141.tyjnwb.top/?cate=0"

    payload = {}
    headers = {
        "Host": "1696006141.tyjnwb.top",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Cookie": "ysmuid=" + ysmuid,
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a28) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print("step1")


def step2():
    url = "https://nsr.zsf2023e458.cloud/yunonline/v1/do_read?uk=" + uk
    payload = {}
    headers = {
        "Host": "nsr.zsf2023e458.cloud",
        "Origin": "https://d1695975741-1258867400.cos.ap-beijing.myqcloud.com",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a28) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.text
    print("step2", response.text)
    data = json.loads(data)
    return data


def step3(url):
    #   url = "http://1695976419.szcoin.site/yunonline/v1/jump?key=eyJpdiI6IkRsc3dBcTBOUng1NWpHOEdKSDh4a2c9PSIsInZhbHVlIjoibDVRUTRxSmVSbzNhcERYa3AwbDVPYWtadVllME41aW9uTzQxaW1zYnhuUUVLSUdHaHp5WU9OSXQrcmlIQk5CNWdIRitGeFZcL0FzMlNQajJoK3RITDc3a0I0bE5IN0lrN01tNExONURtYXRuVldMXC9MSGhDMHZjcTI0Z1Qxazdzd0NEd0tjUXRWKys2V3ZGelwvK1JBdU82MldmZmppb1k5a2FVK1NRU3VXZG96bGY2MDZ5eGoxU1VHakY0QTlyanZEIiwibWFjIjoiMmU4Nzk5MjhkMWRhNWViNjQ1OGViNDVmZDdmNjE4NzM1YzZlZWY0NjNlOGQ2MGMwNzQxMjcyMTFhNzQ2MjFhYSJ9&state=1&unionid=oZdBp05So3-mR3-0TQwJgvAo3iGw?/"

    payload = {}
    headers = {
        "Host": "1695976419.szcoin.site",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "Cookie": "ysmuid=" + ysmuid,
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a28) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print("step3", response.text)


def step4():
    url = (
        "https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?time=30&timestamp="
        + str(time.time())
        + "&uk="
        + uk
    )

    payload = {}
    headers = {
        "Host": "nsr.zsf2023e458.cloud",
        "Origin": "https://d1695975741-1258867400.cos.ap-beijing.myqcloud.com",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a28) NetType/WIFI Language/zh_CN",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    print("step4", data)


def main():
    global uk

    remain_read = remain()
    if remain_read["errcode"] != 0:
        print("获取任务失败！")
        return False
    if remain_read["data"]["remain_read"] == 0:
        print("今日阅读任务完成")
        return False
    time.sleep(random.uniform(3.0,5.0))
    domain = getDomain()
    if domain["errcode"] != 0:
        print("获取阅读链接失败！")
        return False
    domain = domain["data"]["domain"]
    uk = re.findall(r"uk=(.*)&", domain)
    if uk == []:
        print("获取uk失败")
        return False
    uk = uk[0]
    link = step2()
    if link["errcode"] != 0:
        print(link["msg"])
        return False
    time.sleep(random.uniform(3.0,5.0))
    step3(link["data"]["link"])
    time.sleep(random.uniform(3.0,5.0))
    step4()
    return True


if __name__ == "__main__":
    for ysmid in ysmuidList:
        ysmuid = ysmid
        arg = cate()
        if arg["uid"] != []:
            unionid = arg["uid"][0]

        while True:
            task = main()
            if task == False:
                break
        user_gold()
        withdraw(arg)
