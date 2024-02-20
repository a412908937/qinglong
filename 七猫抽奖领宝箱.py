import json
import os
import random
import requests
import time

# 只需要Authorization,写在脚本里就行了,手动挂满听书180分钟就可以,一天跑一次,一定先挂满180分钟再跑
AuthorizationList = os.getenv('qimao_treasure_run')
AuthorizationList = AuthorizationList.split('\n')



# 查余额
def coin(Authorization, t):
	url = "https://api-gw.wtzw.com/welf/h5/v1/task-list"
	headers = {
		"Authorization": eyJhbGciOiJSUzI1NiIsImNyaXQiOlsiaXNzIiwianRpIiwiaWF0IiwiZXhwIl0sImtpZCI6IjE1MzEyMDM3NjkiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3MDk3MTYxMTIsImlhdCI6MTcwODQyMDExMiwiaXNzIjoiIiwianRpIjoiMDZkNTQ3ZjkwYWRkZTZiNjM4ZGI3MjY2ZDhkMmEyOWEiLCJ1c2VyIjp7InVpZCI6NTM5NDM4MzYwLCJuaWNrbmFtZSI6IuS4g-eMq-S5puWPi18xMTIwMTAwNTUxMDIiLCJpbWVpIjoiIiwidXVpZCI6IiIsImRldmljZUlkIjoiIiwicmVnVGltZSI6MTcwMDQ2NjI0NiwidmlwRXhwaXJlQXQiOjAsInNtX2lkIjoiMjAyMDA5MDIwOTUwMjRiYjIwYWFlZGEwZDA4ODBiOGFlMDkzNDQyMTI2MWFjZTAxMTFjNzU3YjAzYjM5MjQiLCJudXQiOjE3MDA0NjYyNjksImlmdSI6MCwiaXNfcmJmIjowLCJhY3RfaWQiOjAsImJpbmRfYXQiOjAsInRpZCI6IkQyZ3VQYXJadVFKVmhLVEE2ZVNPUHBLSXFnWU1GQ1doTTkwMEpPclRzdGZwQVhkZSIsInRfbW9kZSI6Mn19.NTrW3FZ1405Z1EVsfM30KI1XLCemF4B6xhL5-AuDmDfWXHpKHoxs16b3nDdEydkIyf78uYkqv4bLeX5DGTVb3lqhP_yVV7iGJX-c0iosbBNwr4Ca4XP4ysyvjGmgtYrI0OzTVskTMIIaNOuT3_Y0ycQUgGuVrQq-fYqpOe0dZpw
	}
	data = {
		"module_sign": [
			{
				"sign": "9fdefb36c2ec66942d79b1a9a0a8d85d",
				"category": "time_limit"
			},
			{
				"sign": "0d7debfbc25c2184926b23b480bd2450",
				"category": "daily_task"
			}
		],
		"t": t
	}
	getJson = json.dumps(data).encode("utf-8")
	response = requests.post(url=url, headers=headers, data=getJson)
	# print(response.text)
	jsondata = json.loads(response.text)
	result = jsondata["user"]["coin_data"]
	print("余额是" + result + "金币")


# 五次幸运抽奖
def lucky_draw(Authorization, t):
	print("=======开始幸运抽奖=======\r")
	url = "https://xiaoshuo.wtzw.com/api/v2/lucky-draw/do-extractin"
	headers = {
		"Authorization": Authorization
	}
	data = {
		"t": t,
		"apiVersion": 20190309143259 - 1.9
	}
	for i in range(0, 5):
		response = requests.get(url=url, headers=headers, params=data)
		print(response.text)
		time.sleep(random.randint(1, 5))


# 五次幸运7抽奖
def lucky_draw_seven(Authorization, t):
	print("=======开始幸运7抽奖=======\r")
	url = "https://api-gw.wtzw.com/lucky-seven/h5/v1/lottery"
	querystring = {"t": t}
	payload = "source=3&apiVersion=20190309143259 - 1.9"
	headers = {
		"Authorization": Authorization,
		"content-type": "application/x-www-form-urlencoded"
	}
	for i in range(0, 5):
		response = requests.post(url=url, data=payload, headers=headers, params=querystring)
		jsondata = json.loads(response.text)
		#result = jsondata["data"]["title"]
		print(jsondata)
	time.sleep(random.randint(1, 5))


# 领宝箱
def box(Authorization,t):
	print("=======开始领宝箱=======\r")
	url = "https://api-gw.wtzw.com/welf/h5/v1/task/treasure/reward"
	headers = {
		"Authorization": Authorization,
		"content-type": "multipart/form-data;"
	}
	querystring_box = {"t": t}
	response_box = requests.post(url=url, headers=headers, params=querystring_box)
	print(response_box.text)
	time.sleep(random.randint(1, 5))


# 领宝箱视频
def box_video(Authorization,t):
	print("=======开始领宝箱视频=======\r")
	url = "https://api-gw.wtzw.com/welf/h5/v1/task/treasure/video/reward"
	headers = {
		"Authorization": Authorization,
		"content-type": "application/json"
	}
	querystring = {"t": t}
	payload = {
		"position": "welfare_treasurebox_timely",
		"video_prefix": "task_video_two"
	}

	response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
	print(response.text)
	time.sleep(random.randint(1, 5))


# 100次金币
def coin_150():
	print("=======开始领取100次150金币=======\r")
	url = "https://api-ks.wtzw.com/api/v1/coin/add"
	payload = "position_id=inchapter_top&type=6&sign=1"
	headers = {
		"Authorization": Authorization,
		"Host": "api-ks.wtzw.com",
		"Content-Type": "application/x-www-form-urlencoded"
	}
	for i in range(0, 101):
		response = requests.post(url=url, data=payload, headers=headers)
		jsondata = json.loads(response.text)
		print("增加了" + jsondata["data"]["coin"] + "金币", "剩余" + jsondata["data"]["times"] + "次")
		time.sleep(random.randint(1, 5))


def finish_reward(Authorization,t):
	# 113,161
	task_id = [22, 24, 154, 155, 156, 157, 158, 159, 160, 100, 105, 111, 113, 115, 116, 161, 42, 43, 44, 45, 46, 47]
	url = "https://api-gw.wtzw.com/welf/h5/v1/task/finish-task"
	do_url = "https://api-gw.wtzw.com/welf/h5/v1/task/reward"
	headers = {
		"Authorization": Authorization
	}
	for id in task_id:
		data = {
			"t": t,
			"task_id": id

		}
		task_data = {
			"t": t,
			"task_id": id,
			"type_prefix": "task"
		}
		video_data = {
			"t": t,
			"task_id": id,
			"type_prefix": "video"
		}
		if id == 113:
			for i in range(0, 5):
				r4 = requests.post(url=url, headers=headers, data=data)
				print(r4.text)
				time.sleep(random.randint(1, 5))
				r5 = requests.post(url=do_url, headers=headers, data=task_data)
				print(r5.text)
				time.sleep(random.randint(1, 5))
				r6 = requests.post(url=do_url, headers=headers, data=video_data)
				print(r6.text)
				time.sleep(random.randint(1, 5))
		else:
			r1 = requests.post(url=url, headers=headers, data=data)
			print(r1.text)
			time.sleep(random.randint(1, 5))
			r2 = requests.post(url=do_url, headers=headers, data=task_data)
			print(r2.text)
			time.sleep(random.randint(1, 5))
			r3 = requests.post(url=do_url, headers=headers, data=video_data)
			print(r3.text)
			time.sleep(random.randint(1, 5))


if __name__ == '__main__':
	# lucky_draw()
	# coin_150()
	i = 1
	for Authorization in AuthorizationList:
		print(f'------------第{i}个用户------------')
		t = time.time()
		lucky_draw_seven(Authorization,t)
		box(Authorization,t)
		box_video(Authorization,t)
		finish_reward(Authorization,t)
		if i < len(AuthorizationList):
			i += 1
			time.sleep(random.uniform(30,60))
	# coin()
