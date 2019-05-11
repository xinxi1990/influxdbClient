#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
influxdb查询数据
"""

from influxdb import InfluxDBClient
import time,datetime
import random
from pytz import timezone

cst_tz = timezone('Asia/Shanghai')
current_time = (datetime.datetime.now())


class InfluxdbConnect():

    def __init__(self):
        self.client = self.con()


    def con(self):
        '''
        建立连接
        :return:
        '''
        client = InfluxDBClient('localhost', 8086, 'root', 'root', 'api_test')
        client.drop_database('api_test')
        client.create_database('api_test')
        return client


    # def insert_data(self):
    #     for index in range(1000):
    #         code_list = [200, 301, 404, 500]
    #         code = random.choice(code_list)
    #         json_body = [
    #             {
    #                 "measurement": "api_test",
    #                 "tags": {
    #                     "code": code,
    #                     "url": "http://www.baidu.com"
    #                 },
    #                 # "time": "2009-11-10T23:01:00Z",
    #                 "fields": {
    #                     "value": 0 + int(index)
    #                 }
    #             }
    #         ]
    #         self.client.write_points(json_body)
    #         print("====writing data====")


    def insert_data(self,code,url,usetime):

        json_body = [
            {
                "measurement": "api_test",
                "tags": {
                    "code": code,
                    "url": url,
                    "usetime": usetime
                },
                "fields": {
                    "value": 0
                }
            }
        ]
        self.client.write_points(json_body)
        print("====writing data====")

    def query_data(self):
        result = self.client.query('select value from api_test;')
        print("Result: {0}".format(result))

    @staticmethod
    def create_db(db_name):
        client = InfluxDBClient('localhost', 8086, 'root', 'root', db_name)
        client.drop_database(db_name)
        client.create_database(db_name)

if __name__ == '__main__':
    # InfluxdbConnect.create_db("api_test")

    ic = InfluxdbConnect()
    ic.insert_data(200, 1, 1)


