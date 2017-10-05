#!/usr/bin/python
# coding:utf-8
import time
import sys
import os
import Config
from fanpy import * 
from Twitter import update_status,update_with_media
reload(sys)

class Fan:
    def __init__(self):
        self.f = Fanfou(auth=OAuth(
        Config.f_consumer_key, 
        Config.f_consumer_secret, 
        Config.f_access_token,
        Config.f_access_token_secret))
    def get_time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime(time.time()))
    def get_timeline(self):
        msg_list=[]
        msg_img_dic={}
        timeline = self.f.statuses.user_timeline(_id='yihuwang',count=5)
        for tl in timeline:
            try:
                in_reply_to_screen_name= tl['in_reply_to_screen_name']
            except:
                in_reply_to_screen_name=''
            try:
                repost_screen_name = tl['repost_screen_name']
            except:
                repost_screen_name = ''
            if in_reply_to_screen_name:
                continue
            if repost_screen_name:
                continue
            msg = tl['text']
            if msg in msg_set:
                continue
            if 'tw' not in msg:
                continue
            msg_set.add(msg)
            if tl['photo']:
                img_url = tl['photo']['largeurl']
                msg_img_dic[msg]=img_url
            else:
                msg_list.add(msg)
        return msg_list,msg_img_dic

    def run(self):
        while(1):
            print self.get_time()+'go on ...'
            try:
                msg_list,msg_img_dic = self.get_timeline()
                update_status(msg_list)
                update_with_media(msg_img_dic)
            except Exception as e:
                print self.get_time()+"failed !  \n"+ repr(e)
            print self.get_time()+'sleep 10'
            time.sleep(10)
if __name__ == '__main__':
    msg_set=set()
    fan = Fan()
    fan.run()
