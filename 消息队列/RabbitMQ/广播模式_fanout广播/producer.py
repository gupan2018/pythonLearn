# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import sys
import pika
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        'localhost'
    )
)

channel = connection.channel()
# 声明一个exchange，名称为logs，类型是fanout
channel.exchange_declare(
    exchange="logs",
    exchange_type="fanout"
)

msg = "".join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(
    # exchange名称为logs
    exchange='logs',
    # routing_key参数保留，为空
    routing_key='',
    body=msg,
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)

connection.close()
