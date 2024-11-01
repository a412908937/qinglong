#MK集团本部抵制人头王偷CK奥特曼插件从我做起，抵制恶意收费从MK开始。不会做人就让MK教你做人。
import json
import os
import random
import time
import requests
from urllib.parse import quote
from datetime import datetime, date
response = requests.get("https://mkjt.jdmk.xyz/mkjt.txt")
response.encoding = 'utf-8'
txt = response.text
print(txt)

nczlck = os.environ.get('elmjsbck')

ck = ''

def tq(txt):
    try:
        txt = txt.replace(" ", "")
        pairs = txt.split(";")[:-1]
        ck_json = {}
        for i in pairs:
            ck_json[i.split("=")[0]] = i.split("=")[1]
        return ck_json
    except Exception as e:
        print(f'❎Cookie解析错误: {e}')
        return {}


class LYB:
    def __init__(self, cki):
        self.name = None
        self.cki = tq(cki)
        self.uid = self.cki.get("unb")
        self.sid = self.cki.get("cookie2")
        self.token = self.cki.get("token")
        self.deviceId = self.cki.get("deviceId")
        self.host = 'https://acs.m.goofish.com'
        self.name1 = self.uid
        self.success_count = 2

    def xsign(self, api, data, wua, v):
        body = {
            "data": data,
            "api": api,
            "pageId": '',
            "uid": self.uid,
            'sid': self.sid,
            "deviceId": '',
            "utdid": '',
            "wua": wua,
            'ttid': '1551089129819@eleme_android_10.14.3',
            "v": v
        }

        try:
            r = requests.post(
                "sign接口",
                json=body
            )
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as e:
            print(f'❎请求签名服务器失败: {e}')
            return None
        except requests.exceptions.RequestException as e:
            print(f'❎请求签名服务器错误: {e}')
            return None

    def req(self, api, data, wua='False', v="1.0"):
        try:
            if type(data) == dict:
                data = json.dumps(data)
            wua = str(wua)
            sign = self.xsign(api, data, wua, v)
            url = f"{self.host}/gw/{api}/{v}/"
            headers = {
                "x-sgext": quote(sign.get('x-sgext')),
                "x-sign": quote(sign.get('x-sign')),
                'x-sid': self.sid,
                'x-uid': self.uid,
                'x-pv': '6.3',
                'x-features': '1051',
                'x-mini-wua': quote(sign.get('x-mini-wua')),
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'x-t': sign.get('x-t'),
                'x-extdata': 'openappkey%3DDEFAULT_AUTH',
                'x-ttid': '1551089129819@eleme_android_10.14.3',
                'x-utdid': '',
                'x-appkey': '24895413',
                'x-devid': '',
            }

            params = {"data": data}
            if 'wua' in sign:
                params["wua"] = sign.get('wua')

            max_retries = 5
            retries = 0
            while retries < max_retries:
                try:
                    res = requests.post(url, headers=headers, data=params, timeout=5)
                    return res
                except requests.exceptions.Timeout:
                    print("❎接口请求超时")
                except requests.exceptions.RequestException as e:
                    print(f"❎请求异常: {e}")
                retries += 1
                print(f"❎重试次数: {retries}")
                if retries >= max_retries:
                    print("❎重试次数上限")
                    return None
        except Exception as e:
            print(f'❎请求接口失败: {e}')
            return None

    def login(self):
        api1 = 'mtop.alsc.user.detail.query'
        try:
            res1 = self.req(api1, json.dumps({}), 'False', "1.0")
            if res1.json()['ret'][0] == 'SUCCESS::调用成功':
                self.name = res1.json()["data"]["encryptMobile"]
                api = 'mtop.koubei.interaction.center.common.queryintegralproperty.v2'
                data = json.dumps({"templateIds": "[\"1404\"]"})
                try:
                    res = self.req(api, data, 'False', "1.0")
                    if res.json()['ret'][0] == 'SUCCESS::调用成功':
                        print(f'[{self.name}] ✅登录成功,乐园币----[{res.json()["data"]["data"]["1404"]["count"]}]')
                        return True
                    else:
                        if res.json()['ret'][0] == 'FAIL_SYS_SESSION_EXPIRED::Session过期':
                            print(f"[{self.name1}] ❎cookie已过期，请重新获取")
                            return False
                        else:
                            print(f'[{self.name1}] ❌登录失败,原因:{res.text}')
                            return False
                except Exception as e:
                    print(f"[{self.name1}] ❎登录失败: {e}")
                    return False
            else:
                if res1.json()['ret'][0] == 'FAIL_SYS_SESSION_EXPIRED::Session过期':
                    print(f"[{self.name1}] ❎cookie已过期，请重新获取")
                    return False
                else:
                    print(f'[{self.name1}] ❌登录失败,原因:{res1.text}')
                    return False
        except Exception as e:
            print(f"[{self.name1}] ❎登录失败: {e}")
            return False

    def yqm(self):
        api = 'mtop.ele.biz.growth.task.core.querytask'
        data = json.dumps({"bizScene":"ORCHARD_FAST","missionCollectionId":"423","accountPlan":"HAVANA_COMMON","locationInfos":"[\"{\\\"lng\\\":\\\"120.57360671460629\\\",\\\"lat\\\":\\\"28.036069851368666\\\"}\"]"})

        try:
            res = self.req(api, data, 'False', "1.0")
            
            if res is None:
                return None, None
            if res.json()["ret"][0] == "SUCCESS::接口调用成功":
                for entry in res.json().get("data", {}).get("mlist", []):
                    action_config = entry.get("actionConfig", {})
                    if action_config.get("missionInstanceTriggerType") == 'P2P' and action_config.get("actionValue", {}).get("p2pType") == 'SHARE':
                        ext = action_config.get("ext", {})
                        actId = ext.get("actId")
                        shareId = ext.get("shareId")
                    
                        if actId and shareId:
                            print(f'{actId}')
                        return actId, shareId
                else:
                    if res.json()["ret"][0] == "FAIL_SYS_SESSION_EXPIRED::Session过期":
                        print("❎cookie已过期，请重新获取")
                        return None, None
                    else:
                        print(res.text)
                        return None, None
        except Exception:
            print(f'❎请求错误')
            return None, None

            
            
    def share(self, actid1, shareId1):
        
        
        api = 'mtop.alsc.play.component.snsshare.trigger.risk'
        data = json.dumps({"bizScene": "ORCHARD_FAST", "shareId": shareId1, "actId": actid1,"asac":"2A20B11ERAXCI9D3X4L8ZW"})
        try:
            res = self.req(api, data, 'False', "1.0")
            if res is None:
                return None
            if res.json()["ret"][0] == "SUCCESS::接口调用成功":
                self.success_count += 1  # 助力成功，增加成功次数
                print(f"[{self.name1}] ✅助力成功")
                
                if self.success_count >= 3:  # 如果今日助力成功3次，则跳过当前账号
                    print(f"[{self.name1}] ❎今日助力已达上限，跳过当前账号")
                    return 'SX'
                return True
                
                    
            else:
                if res.json()["ret"][0] == "FAIL_SYS_SESSION_EXPIRED::Session过期":
                    print(f"[{self.name1}] ❎cookie已过期，请重新获取")
                    return False
                else:
                    if res.json()["ret"][0] == "助力次数已用完":
                        print(f"[{self.name1}] ❎助力次数已用完")
                        return False
                    if res.json()["ret"][0] == "今日助力次数已用完":
                        print(f"[{self.name1}] ❎哦豁，莫得次数咯")
                        return False
                    if res.json()["ret"][0] == "SNS_RELATION_SELF:: 人传人关系是本人":
                        print(f"[{self.name1}] ❎不可给自己助力")
                        return None
                    if res.json()["ret"][0] == "SNS_RELATION_LIMIT_ERROR:: 人传人关系已达上限":
                        print(f"[{self.name1}] ❎助力上限\n")
                        return 'SX'
                    if res.json()["ret"][0] == " 人传人关系已达上限":
                        print(f"[{self.name1}] ❎助力上限\n")
                        return 'SX'
                    if res.json()["ret"][0] == "分享者已被助力成功，客态重复助力":
                        print(f"[{self.name1}] ❎重复助力")
                        return None
                    else:
                        print(f"[{self.name1}] ❎助力失败")
                        print(res.text)
                        return None
        except Exception as e:
            print(f'请求错误', e)
            return None


    
 

    def pk(self):
        def task():
            api = 'mtop.ele.biz.growth.task.core.querytask'
            data2 = json.dumps({"bizScene":"ORCHARD_FAST","missionCollectionId":"423","accountPlan":"HAVANA_COMMON","locationInfos":"[\"{\\\"lng\\\":\\\"120.57360671460629\\\",\\\"lat\\\":\\\"28.036069851368666\\\"}\"]"})

            try:
                res3 = self.req(api, data2, 'False', "1.0")
                
                for tag_data in res3.json()["data"]["mlist"]:
                    for y in tag_data["missionStageDTOS"]:
                        if y["rewardStatus"] != "SUCCESS":
                            skip_keywords = [
                                             '外卖实付7元以上送达领水滴' ]
                            skip_task = False
                            for keyword in skip_keywords:
                                if keyword in tag_data["showTitle"]:
                                    skip_task = True
                                    break
                            if skip_task:
                                continue
                            name2 = tag_data["showTitle"]
                            missionDefId1 = tag_data["missionDefId"]
                            instanceId = tag_data.get("id", "")
                            if tag_data["showTitle"] == "在页面内点击3个店铺":
                                count = '3'
                            elif tag_data["showTitle"] == "浏览外卖品质好店":
                                count = '2'
                            
                            
                            else:
                                count = '1'
                            pageSpm = tag_data["actionConfig"]["actionValue"].get("pageSpm", "")
                            pageStageTime = tag_data["actionConfig"]["actionValue"].get("pageStageTime", "")
                            api = 'mtop.ele.biz.growth.task.event.pageview'
                            payload = {
                                "bizScene": "ORCHARD_FAST",
                                "accountPlan": "HAVANA_COMMON",
                                "collectionId": "432",
                                "missionId": missionDefId1,
                                "actionCode": "PAGEVIEW",
                                "asac": "2A20B11WIAXCI9QYYXRIR0",
                                "sync": "false"
                            }
                            if pageSpm:
                                payload['pageFrom'] = pageSpm
                            if pageStageTime:
                                payload['viewTime'] = pageStageTime
                            data2 = json.dumps(payload)
                            res3 = self.req(api, data2, 'False', "1.0")
                            
                            if res3.json()["ret"][0] == "SUCCESS::接口调用成功":
                                print(f"[{self.name}] ✅[{name2}]任务完成")
                                which(name2, missionDefId1,instanceId, count)
                            else:
                                print(f"[{self.name}] ❎完成任务失败: {res3.json()['ret'][0]}")
            except Exception as e:
                print(f"发生错误: {e}")

        
    

        def which(name2, missionDefId1,instanceId, count):
            if name2 != '邀请好友助力' and count != '6':
                for i1 in range(1, int(count) + 1):
                    api = 'mtop.ele.biz.growth.task.core.receiveprize'
                    data1 = json.dumps({
        "missionCollectionId": "423",
        "missionId": str(missionDefId1),
        "instanceId": str(instanceId),
        "count": str(i1),  # 这里应该是 count 而不是 i1
        "bizScene": "ORCHARD_FAST",
        "accountPlan": "HAVANA_COMMON",
        "locationInfos": "[{\"lng\":\"120.57360671460629\",\"lat\":\"28.036069851368666\"}]"
        })
                    res3 = self.req(api, data1, 'False', "1.0")
                    if res3.json()["ret"][0] == "SUCCESS::接口调用成功":
                    
                        print(f"[{self.name}] ✅[{name2}]奖励领取成功")
                        
                    else:
                        print(f"[{self.name}] ❎[{name2}]奖励领取失败: {res3.json()['ret'][0]}")
                        return False
            elif '邀请好友助力' in name2 or name2 == '邀请好友助力':
                 api = 'mtop.ele.biz.growth.task.core.receiveprize'
                 data1 = json.dumps({
        "missionCollectionId": "423",
        "missionId": str(missionDefId1),
        "instanceId": str(instanceId),
        "count": str(count),  # 这里应该是 count 而不是 i1
        "bizScene": "ORCHARD_FAST",
        "accountPlan": "HAVANA_COMMON",
        "locationInfos": "[{\"lng\":\"120.57360671460629\",\"lat\":\"28.036069851368666\"}]",
        "asac":"2A20B11WIAXCI9QYYXRIR0"
        })
                 
                 res3 = self.req(api, data1, 'False', "1.0")
                 if res3.json()["ret"][0] == "SUCCESS::接口调用成功":
                     print(f"[{self.name}] ✅[{name2}]奖励领取成功")
                     
                 else:
                     print(f"[{self.name}] ❎[{name2}]奖励领取失败: {res3.json()['ret'][0]}")
                     return False
       
            

        task()
    def roleId(self):
        api = 'mtop.alsc.playgame.orchard.index.query'
        data = json.dumps({"bizScene":"ORCHARD_FAST","indexType":"ORCHARD_FAST_INDEX"})

        try:
            res = self.req(api, data, 'False', "1.0")
            
            
            
            if res.json()["ret"][0] == "SUCCESS::调用成功":
                for role_info in res.json().get("data", {}).get("data", {}).get("roleInfoDtoList", []):
                    if role_info.get("roleBaseInfoDto", {}).get("roleName") == '极速水果':
                        prizeNumId = role_info.get("roleBaseInfoDto", {}).get("roleId")
                        
                                
                        self.task2(prizeNumId)
                            
        except Exception as e:
            print(f"[{self.name}] ❎请求错误{e}")
            return None


    def task2 (self,prizeNumId):
        max_retries = 20
        retries = 0
        while retries < max_retries:
            api = 'mtop.alsc.playgame.orchard.roleoperate.useprop'
            data = json.dumps({"bizScene":"ORCHARD_FAST","roleId":"" + prizeNumId + "","propertyTemplateId":"1266"})
            
            res = self.req(api, data, 'False', "1.0")
            if res.json()["ret"][0] == "SUCCESS::调用成功":
                
                
                retries += 1
                print(f'[{self.name}]----浇水成功')
            else:
                if res.json()["ret"][0] == "FAIL_SYS_SESSION_EXPIRED::Session过期":
                    print("❎cookie已过期，请重新获取")
                    return False
                else:
                    print(f"[{self.name}]----浇水失败，原因:{res.json()['ret'][0]}")
                    return False
    

    
    def main(self):
        try:
            if self.login():
               
                self.pk()
                self.roleId()
        except Exception as e:
            print(f"[{self.name1}] 请求错误{e}")


def get_ck_usid(ck1):
    try:
        key_value_pairs = ck1.split(";")
        for pair in key_value_pairs:
            key, value = pair.split("=")
            if key.lower() == "userid":
                return value
    except Exception:
        return 'y'


if __name__ == '__main__':
    today = date.today()
    today_str = today.strftime('%Y%m%d')
    filename = f'{today_str}ncjsb.json'
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump({}, f)
        print("今日助力json文件不存在，已创建")
    else:
        print("今日助力json文件已存在")

    with open(filename, 'r') as file:
        data = json.load(file)

    if 'elmck' in os.environ:
        cookie = os.environ.get('elmck')
    else:
        print("❎环境变量中不存在[elmck],启用本地变量模式")
        cookie = ck
    if cookie == "":
        print("❎本地变量为空，请设置其中一个变量后再运行")
        exit(-1)
    cookies = cookie.split("&")

    zlck_list = nczlck.split("&")
    print(f"获取到 {len(zlck_list)} 个被助力账号")

    dzl_num = 0
    for zlck in zlck_list:
        dzl_num += 1
        lyb = LYB(zlck)
        actid, shareId = lyb.yqm()
        if actid is None or shareId is None:
            
            print("❎获取助力id失败")
            
        else:
            print(f"======被助力账号{dzl_num}获取邀请码成功,开始助力======")
            for i, ck in enumerate(cookies):
                usid = get_ck_usid(ck)
                zlcs = data.get(f"{usid}", 0)
                if zlcs < 1:
                    print(f"======被助力账号{dzl_num}-开始第{i + 1}/{len(cookies)}个账号助力======")
                    a = LYB(ck).share(actid, shareId)
                    if a == 'SX':
                        break
                    elif a:
                        data[f"{usid}"] = zlcs + 1
                        with open(filename, 'w') as file:
                            json.dump(data, file, indent=4)
                        print("2s后进行下一个账号")
                        time.sleep(2)
                        continue
                    elif a is False:
                        data[f"{usid}"] = 1
                        with open(filename, 'w') as file:
                            json.dump(data, file, indent=4)
                        print("2s后进行下一个账号")
                        time.sleep(2)
                        continue
                    else:
                        print("2s后进行下一个账号")
                        time.sleep(2)
                        continue
                else:
                    continue
        print(f"======被助力账号{dzl_num}-领取奖励并浇水======")
        lyb.main()
        print(f"======被助力账号{dzl_num}-任务结束======\n\n")
