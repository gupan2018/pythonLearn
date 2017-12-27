# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import pika
user_pwd = pika.PlainCredentials("admin", '123456')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.17.136',
                              credentials=user_pwd)
)

channel = connection.channel()
channel.queue_declare(queue="queue_test1", durable=True)
channel.basic_publish(
    exchange='',
    routing_key='queue_test1',
    body='hello',
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)

connection.close()
