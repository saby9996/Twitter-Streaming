# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:40:24 2018

@author: sabyasachi.ch
"""

import json
import pandas as pd
 
tweet_files = [INPUT FILE PATH]
tweets = []
for file in tweet_files:
    with open(file, 'r') as f:
        for line in f.readlines():
            tweets.append(json.loads(line))
            
def populate_tweet_df(tweets):
    df = pd.DataFrame()
    df['id'] = list(map(lambda tweet: tweet['id'], tweets))
    df['created_at']= list(map(lambda tweet: tweet['created_at'], tweets))
    df['text'] = list(map(lambda tweet: tweet['text'], tweets))
    df['user_name']=list(map(lambda tweet: tweet['user']['name'], tweets))
    df['screen_name']=list(map(lambda tweet: tweet['user']['screen_name'], tweets))
    df['followers_count']=list(map(lambda tweet: tweet['user']['followers_count'], tweets))
    df['friends_count']=list(map(lambda tweet: tweet['user']['friends_count'], tweets))
    df['user_creation']=list(map(lambda tweet: tweet['user']['created_at'], tweets))
    df['time_zone']=list(map(lambda tweet: tweet['user']['time_zone'], tweets))
    df['location'] = list(map(lambda tweet: tweet['user']['location'], tweets))
    df['country_code'] = list(map(lambda tweet: tweet['place']['country_code'] if tweet['place'] != None else '', tweets))
    df['long'] = list(map(lambda tweet: tweet['coordinates']['coordinates'][0] if tweet['coordinates'] != None else 'NaN', tweets))
    df['latt'] = list(map(lambda tweet: tweet['coordinates']['coordinates'][1] if tweet['coordinates'] != None else 'NaN', tweets))
    return df

data=populate_tweet_df(tweets)
data.to_csv(OUTPUT FILE PATH, header=True)
