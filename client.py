#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author  : xinxi
@Time    : 2018/1/17 20:02
@describe:

"""
import requests,json,yaml,os,datetime,subprocess,sys,time

request_log = "api.log"


class Client():

    def request_api(self):
        r = requests.get('http://wwww.baidu.com')
        use_time = int(str(r.elapsed).split('.')[-1])
        now = int(time.time())
        with open(request_log, 'a') as f_w:
            f_w.write(str(now) + ','+ str(use_time) + '\n')
            print('写{}文件完成'.format(request_log))


if __name__ == '__main__':
    for index in range(1000):
        time.sleep(0.5)
        Client().request_api()
