# -*- coding: utf-8 -*-

import requests
import random
import json
from hashlib import md5


def get_translate_results(query):
    # 百度申请的appid和appkey填在这里
    appid = ''
    appkey = ''

    from_lang = 'en'
    to_lang = 'zh'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    r = requests.post(url, params=payload, headers=headers)
    result = r.json().get('trans_result')
    r = ''
    for res in result:
        r = r + res.get('dst') + '\n'
    # Show response
    return r
