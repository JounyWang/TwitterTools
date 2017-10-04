# -*- coding: utf-8 -*-
# @Author: jouny
# @Date:   2017-10-04 22:07:45
# @Last Modified by:   jouny
# @Last Modified time: 2017-10-04 22:56:04
import tweepy,Config
auth = tweepy.OAuthHandler(Config.consumer_key, Config.consumer_secret)
auth.set_access_token(Config.access_token, Config.access_token_secret)
api = tweepy.API(auth)
api.update_status(status="test again and again")