#import notify
#答题模型申请https://xinghuo.xfyun.cn/sparkapi?scr=true 13行输入api密码
#环境变量bjhb CK格式:备注#xtoken 多号换行
#小程序://每天喜乐多/K3INVzGVFQoTM4B
import requests, json, re, os, sys, time, random, datetime, execjs
response = requests.get("https://mkjt.jdmk.xyz/mkjt.txt")
response.encoding = 'utf-8'
txt = response.text
print(txt)
environ = "bjxld"
name = "北京༒喜乐多"
session = requests.session()
#---------------------主代码区块---------------------
def request_chatgpt_function(question):
    model = "lite"
    url = "https://spark-api-open.xf-yun.com/v1/chat/completions"
    APIPassword = ""

    header = {"Content-Type": "application/json", "Authorization": f"Bearer {APIPassword}"}
    prompt = "你是知识渊博的助理。"
    data={"model": model,"messages": [{"role": "system","content": prompt},{"role": "user","content": f"{question}；请给出答案，只要字母"}],"temperature": 0}
    response = requests.post(url=url, headers=header, json=data).json()
    if response.get('choices'):
        result = response['choices'][0]['message']['content']
        # 使用正则表达式提取第一个大写字母，答题专用
        match = re.search(r'[A-D]', result)
        if match:
            result = match.group()
        else:
            return False
        #print(result)
        return result
    else:
        print(response)
        return False

def run(x_token):
    try:
        header = {
        "Accept": "*/*",
        "Accept-language": "zh-CN,zh;q=0.9",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/11581",
        "Content-length": "2",
        "Content-type": "application/json;charset=UTF-8",
        "xweb_xhr": "1",
        "x-token": x_token,
        "Sec-fetch-dest": "empty",
        "Sec-fetch-mode": "cors",
        "Sec-fetch-site": "cross-site",
        "Connection": "keep-alive",
        "Host": "xld-api.bjsfxh.com",
        }
        url = 'https://xld-api.bjsfxh.com/api/getUserInfo'
        response = session.post(url=url, headers=header, json={}).json()
        userInfo = response["data"]["userInfo"]
        print(f"☁️{userInfo['nickname']}：{userInfo['levelName']}")
        url = 'https://xld-api.bjsfxh.com/api/userSign'
        response = session.post(url=url, headers=header, json={}).json()
        if "已签到" in response["message"] or "ok" in response["message"]:
            print("☁️签到状态：已签到")
        url = 'https://xld-api.bjsfxh.com/api/home'
        response = session.post(url=url, headers=header, json={}).json()
        #print(response)
        for i in response.get("data",{}).get("activity",[]):
            statusView = i.get("statusView")
            next = False
            if "进行中" in statusView:
                id = i.get("id")
                #title = i.get("title")
                titlestart = i.get("title").split("·")[0].split("｜")[1].rsplit("第")[-2][:3]
                titleend = i.get("title").split("·")[0].split("｜")[1].rsplit("第")[-1]
                print(f"\n---🌥️{titlestart}-{titleend}🌥️---\n☁️开 始 静 默 答 题")
                #print(f"\n---🌥️{title}🌥️---\n☁️开 始 静 默 答 题")
                for m in range(5):
                    for n in range(20):
                        if n == 0:
                            url = "https://xld-api.bjsfxh.com/api/startAnswer"
                            data = {"id": id}
                        else:
                            url = "https://xld-api.bjsfxh.com/api/getQuestion"
                            data = {"id": id, "examId": examId, "number": n + 1}
                        response = requests.post(url=url, headers=header, json=data).json()
                        #print(response)
                        if "用户未认证或未添加企微" in response.get("message", ""):
                            print(f"⭕未认证或未添加企微")
                            next = True
                            break
                        elif "此活动参与次数已达上限" in response.get("message",""):
                            print(f"⭕活动参与次数已上限")
                            next = True
                            break
                        else:
                            explain = response["data"]["question"]["explain"]
                            body = response["data"]["question"]["body"]
                            options=""
                            for op in response["data"]["question"]["options"]:
                                label=op["label"]
                                value=op["value"]
                                options=f"{options} {label}:{value}"
                            quest=f"以下是题目:{body}；题目的提示:{explain}；题目的选项:{options}，请输出答案"
                            #print(quest)
                            answer=request_chatgpt_function(quest)
                            if not answer:
                                return
                            if n == 0:
                                examId = response["data"]["examId"]
                            url = "https://xld-api.bjsfxh.com/api/submitAnswer"
                            data = {"examId": examId, "id": id, "answer": answer, "number": n + 1}
                            submitAnswer = requests.post(url=url, headers=header, json=data).json()
                            #print(f"第{n + 1}题回答：{answer}答题结果：", submitAnswer["data"]["isCorrect"])
                        questionNum = response["data"]["questionNum"]
                        if int(questionNum)-1==n:
                            break
                        time.sleep(random.randint(1, 2))
                    if next:
                        break
                    else:
                        url = "https://xld-api.bjsfxh.com/api/submitExam"
                        data = {"id":id,"examId":examId}
                        response = requests.post(url=url, headers=header, json=data).json()
                        #print(f"交卷：{response['message']}")
                        url = "https://xld-api.bjsfxh.com/api/examResult"
                        data = {"id":id,"examId":examId}
                        response = requests.post(url=url, headers=header, json=data).json()
                        #print(f"交卷结果：{response['message']}")
                        url = "https://xld-api.bjsfxh.com/api/lottery"
                        data = {"id":id,"examId":examId}
                        for _ in range(5):
                            response = requests.post(url=url, headers=header, json=data).json()
                            isCanAgain = response["data"]["isCanAgain"]
                            isWin = response["data"]["isWin"]
                            try:
                                if isWin:
                                    money = response["data"]["money"]
                                    print(f"🌈抽奖结果：{money} 现金")
                                else:
                                    #print(f'⭕抽奖结果：未中奖呦')
                                    pass
                                if not isCanAgain:
                                    break
                            except:
                                print(f'⭕抽奖异常:{response}')
                            time.sleep(30)
        url = 'https://xld-api.bjsfxh.com/api/getUserInfo'
        totalMoney = session.post(url=url, headers=header, json={}).json()["data"]["userInfo"]['totalMoney']
        url = 'https://xld-api.bjsfxh.com/api/getUserActivity'
        response = session.post(url=url, headers=header, json={"page":1}).json()
        items = response["data"]["items"]
        money = 0
        for i in items:
            endAt = i["endAt"]
            if datetime.datetime.fromtimestamp(endAt).day == datetime.datetime.now().day:
                money = money + float(i["money"])
        print(f"--------------------\n☁️累计获得：{totalMoney}元\n🌈今日获得：{money:.1f}元")
    except Exception as e:
        print(e)

def main():
    global header
    if os.environ.get(environ):
        ck = os.environ.get(environ)
    else:
        ck = ""
        if ck == "":
            print("请设置变量")
            sys.exit()
    ck_run = ck.split('\n')
    ck_run = [item for item in ck_run if item]
    print(f"{' ' * 10}꧁༺ {name} ༻꧂\n")
    for i, ck_run_n in enumerate(ck_run):
        print(f'\n----------- 🍺账号【{i + 1}/{len(ck_run)}】执行🍺 -----------')
        try:
            id,x_token = ck_run_n.split('#',1)
            #id = id[:3] + "*****" + id[-3:]
            print(f"📱：{id}")
            run(x_token)
            #time.sleep(random.randint(1, 2))
        except Exception as e:
            print(e)
            #notify.send('title', 'message')
    print(f'\n----------- 🎊 执 行  结 束 🎊 -----------')

if __name__ == '__main__':
    main()