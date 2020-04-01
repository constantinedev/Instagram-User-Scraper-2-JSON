import os
import sys
import bs4
import codecs
import json
import time
import schedule
import subprocess

def IG_SCRAP():
    user_list = open('IG_user_List.txt', 'r')
    while True:
        username = user_list.readline().strip('\n')
        key = "/?__a=1"
        query_url = "https://www.instagram.com/" + username + key
        
        if not username:
            break
        output_dir = "ig_user_dumper/" + username + "_log.json"
        #print (query_url)
        #print (username)
        #print (output_dir)
        dumper = subprocess.call(['wget', '-O', output_dir, query_url])
    user_list.close()

schedule.every(1).hour.do(IG_SCRAP)

while True:
    schedule.run_pending()
    time.sleep(10)