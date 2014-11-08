# -*- coding: utf-8 -*-
"""
Created on 08.01.2013 12:55:29
@author: Oleksandr Poliatykin
"""
import requests

r = requests.get('http://ya.ru', timeout=1)

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)

