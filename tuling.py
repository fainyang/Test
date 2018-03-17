# -*- coding=utf-8 -*-
import requests
import itchat
import random
from itchat.content import *

KEY = '543bc357ffd4425da2a02db84320a72a'

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
def group_id(name): #找到群ID
    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']

#自定义机器人后缀
robots=['——[Pup]机器人[Pup]','——[Pup]急事语音通话[Pup]','——[Pup]不是本人[Pup]']

@itchat.msg_register(TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply
    # a or b的意思是，如果a有内容，那么返回a，否则返回b

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def picture_reply(msg):
    pic=str(random.randint(1,4))
    itchat.send('@img@%s' % (pic+'.jpg'),msg['FromUserName'])
    #从本地随机选择一张图片发送 '@img@图片地址'将会被识别为传送图片

@itchat.msg_register([TEXT,PICTURE], isGroupChat=True)
def group_text_reply(msg):
    # 当然如果只想针对@你的人才回复，可以设置if msg['isAt']: 
    #item = group_id('🦀️一只螃蟹，两只螃蟹🦀️')  # 根据自己的需求设置特定回复群
    if msg['isAt'] :
        reply = get_response(msg['Text'])+random.choice(robots)
        itchat.send('%s' % reply,msg['FromUserName'] )
    '''
    #定点在某几个群里斗图
    if msg['Type']=='Picture' and \
    (msg['FromUserName']== group_id('🦀️一只螃蟹，两只螃蟹🦀️') or \
    msg['FromUserName']== group_id('科大泸州程序猿交流群') or \
    msg['FromUserName']== group_id('沉迷学习，日渐消瘦') ): 
        pic=str(random.randint(1,4))
        itchat.send('@img@%s' % (pic+'.jpg'),msg['FromUserName'])
    '''
itchat.auto_login() #enableCmdQR=True
itchat.run()