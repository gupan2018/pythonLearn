# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import pika
user_pwd = pika.PlainCredentials("admin", '123456')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.17.136',
                              credentials=user_pwd)
)

channel = connection.channel()
# 声明一个exchange，名称为logs，类型为fanout
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

# 随机生成一个消息队列
result = channel.queue_declare(exclusive=True)
# 获取随机生成的消息队列名称
queue_name = result.method.queue
# 绑定消息队列到exchange
channel.queue_bind(
    exchange='logs',
    queue=queue_name
)

def callback(ch, method, properties, body):
    print("received msg:", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

consume = channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=False)
channel.start_consuming()
