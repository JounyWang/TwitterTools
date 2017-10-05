# -*- coding: utf-8 -*-
# @Author: jouny
# @Date:   2017-10-04 22:07:45
# @Last Modified by:   jouny
# @Last Modified time: 2017-10-06 00:24:46
import tweepy,Config,time,urllib
auth = tweepy.OAuthHandler(Config.t_consumer_key, Config.t_consumer_secret)
auth.set_access_token(Config.t_access_token, Config.t_access_token_secret)
api = tweepy.API(auth)
def get_time():
	return time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime(time.time()))
def update_status(msg_list):
	if len(msg_list):
		for msg in msg_list:
			try:
				api.update_status(status=msg)
				print get_time()+'update_status sucess'
			except Exception as e:
				print get_time()+'update_status failed  \n'+ repr(e)
	else:
		print 'msg_list nothing'
def update_with_media(msg_img_dic):
	if len(msg_img_dic):
		try:
			for key in msg_img_dic.keys():
				urllib.urlretrieve(msg_img_dic[key], "image.jpg")
				print get_time()+'image.jpg done'
				api.update_with_media(filename='image.jpg',status=key)
				print get_time()+'update_with_media sucess'
		except  Exception as e:
			print get_time()+'update_with_media failed  \n'+ repr(e)
	else:
		print 'msg_img_dic nothing'
	