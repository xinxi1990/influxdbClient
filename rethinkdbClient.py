#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
rethinkdb查询数据
"""


from rethinkdb import RethinkDB



class dbOperation():
    '''
    同步写入模式
    '''

    def __init__(self,dbname,tablename):
        r = RethinkDB()
        self.conn = r.connect(host="localhost",port=28015)
        try:
            r.table_create('marvel').run(self.conn)
        except Exception as e:
            print(e)
        self.table = r.db(dbname).table(tablename)

    def insert(self,document):
        '''
        插入记录到数据库
        '''
        return self.table.insert(document, conflict="update").run(self.conn)


    def query(self,**kwargs):
        '''
        自定义查询
        '''
        f=self.table.run(self.conn)  ##选择网站名称为空的记录。
        content=[]
        for i in f:
            content.append(i)
        return content



import asyncio
from rethinkdb import RethinkDB

class gevent_dbOperation():

    '''
    异步写入模式
    '''
    def __init__(self,dbname,tablename):
        r = RethinkDB()
        r.set_loop_type('asyncio')
        self.conn = r.connect(host="localhost",port=28015)
        try:
            r.table_create('marvel').run(self.conn)
        except Exception as e:
            print(e)
        self.table = r.db(dbname).table(tablename)

    async def insert(self,document):
        '''
        插入记录到数据库
        '''

        return await self.table.insert(document, conflict="update").run(self.conn)


    def query(self,**kwargs):
        '''
        自定义查询
        '''
        f=self.table.run(self.conn)  ##选择网站名称为空的记录。
        content=[]
        for i in f:
            content.append(i)
        return content



if __name__ == '__main__':
    document = {
        'id': 1,
        'name': 'Iron Man',
        'first_appearance': 'Tales of Suspense #39'
    }

    #
    # dbt = dbOperation("test","marvel")
    # for index in range(10):
    #     result = dbt.insert(document)
    #     print("插入数据:第{}次".format(index))
    #     print("插入结果:{}".format(result))

    # dbt = gevent_dbOperation("test", "marvel")
    # for index in range(10):
    #     result = dbt.insert(document)
    #     print("插入数据:第{}次".format(index))
    #     print("插入结果:{}".format(result))

    asyncio.get_event_loop().run_until_complete(gevent_dbOperation("test", "marvel").insert(document))


    for hero in dbt.query():
        print(hero['name'])






