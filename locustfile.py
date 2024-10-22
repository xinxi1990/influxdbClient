#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
locust并发
定义用户行为，继承TaskSet类，用于描述用户行为
(这个类下面放各种请求，请求是基于requests的，每个方法请求和requests差不多，请求参数、方法、响应对象和requests一样的使用，url这里写的是路径)
client.get===>requests.get
client.post===>requests.post
"""

import time
from locust import HttpLocust, TaskSet, task
from Influxdbcon import InfluxdbConnect

ic = InfluxdbConnect()

request_log = "api.log"

class test_126(TaskSet):
    '''
    task装饰该方法为一个事务方法的参数用于指定该行为的执行权重。
    参数越大，每次被虚拟用户执行概率越高，不设置默认是1，
    '''
    @task()
    def test_baidu(self):
        # 定义requests的请求头
        header = {"User-Agent": "Mozilla/5.0 "
                                "(Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                                "(KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
        # r是包含所有响应内容的一个对象
        r = self.client.get("/", timeout=30, headers=header)
        # 这里可以使用assert断言请求是否正确，也可以使用if判断
        use_time = float(str(r.elapsed).split(':')[-1])
        url = r.url
        code  = r.status_code
        ic.insert_data(code,url,use_time)
        now = int(time.time())
        with open(request_log, 'a') as f_w:
            f_w.write(str(now) + ','+ str(use_time) + '\n')
            print('写{}文件完成'.format(request_log))
        assert r.status_code == 200


class websitUser(HttpLocust):
    '''
    这个类类似设置性能测试，继承HttpLocust
    '''
    # 指向一个上面定义的用户行为类
    task_set = test_126
    # 执行事物之间用户等待时间的下界，单位毫秒，相当于lr中的think time
    min_wait = 3000
    max_wait = 6000

