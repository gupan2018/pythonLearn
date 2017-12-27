# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import pika
user_pwd = pika.PlainCredentials("admin", '123456')
# 相当于建立一个socket
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.17.136',
                              credentials=user_pwd)
)

# 申明一个管道，在管道里发消息
channel = connection.channel()


# 声明一个queue，队列名为hello
channel.queue_declare(queue='hello')

# 通过管道发送消息
channel.basic_publish(exchange='',
                      # queue名字
                      routing_key='hello',
                      body='Hello World')

print("[x] sendt 'Hello World'")
# 不用关闭管道，直接关闭队列即可
connection.close()