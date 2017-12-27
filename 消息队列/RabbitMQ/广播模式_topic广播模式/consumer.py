# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import sys
import pika

user_pwd = pika.PlainCredentials("admin", '123456')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.17.136',
                              credentials=user_pwd)
)

channel = connection.channel()
# 声明一个exchange，名称为logs，类型为fanout
channel.exchange_declare(
    exchange='logs_02',
    exchange_type='topic'
)

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

bonding_keys = sys.argv[1:]

if not bonding_keys:
    sys.stderr.write("Usage : %s [bingding_key] ...\n" % sys.argv[0])
    sys.exit(1)

for bonding_key in bonding_keys:
    channel.queue_bind(
        exchange='logs_02',
        queue=queue_name,
        routing_key=bonding_key
    )

def callback(ch, method, properties, body):
    print("%s received msg: %r" % (method.routing_key, body))

channel.basic_consume(
    consumer_callback=callback,
    queue=queue_name,
    no_ack=True)
channel.start_consuming()