# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

# 声明一个queue，队列名为hello，进行持久化
channel.queue_declare(queue='hello1', durable=True)
channel.basic_publish(exchange='',
                      routing_key='hello1',
                      body='Hello Worldvbdsb',
                      # 持久化队列中的消息
                      properties=pika.BasicProperties(
                          delivery_mode=2
                      )
                      )

print("[x] sendt 'Hello World'")
connection.close()