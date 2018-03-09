# -*- coding=utf-8 -*-
import requests
import itchat
import random

KEY = 'xxxxxxxxxxxxxxxx'#去图灵机器人网注册一个，得到apikey。

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots=['——By机器人','——有急事打call','——By反正不是本人']
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply
#enableCmdQR 在命令窗口显示二维码，如果改为itchat.auto_login()，则为系统弹出窗口显示二维码
#但是Centos 没有图形化界面，只能命令窗口显示二维码
itchat.auto_login(enableCmdQR=2) #enableCmdQR=True
itchat.run()