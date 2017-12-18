# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import pika

# 相当于建立一个socket
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

# 申明一个管道，在管道里发消息
channel = connection.channel()


# 声明一个queue，队列名为hello，进行持久化
channel.queue_declare(queue='hello', durable=True)

# 通过管道发送消息
channel.basic_publish(exchange='',
                      # queue名字
                      routing_key='hello',
                      body='Hello World',
                      # 持久化队列中的消息
                      properties=pika.BasicProperties(
                          delivery_mode=2
                      ))

print("[x] sendt 'Hello World'")
# 不用关闭管道，直接关闭队列即可
connection.close()