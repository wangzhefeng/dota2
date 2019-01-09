#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json

url = "https://api.opendota.com/api"
headers = {
	'accept-language': 'zh-CN,zh;q=0.9',
	'origin': 'https://docs.opendota.com',
	'referer': 'https://docs.opendota.com/',
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


response = requests.get(url = url, headers = headers)
print(response.text)
