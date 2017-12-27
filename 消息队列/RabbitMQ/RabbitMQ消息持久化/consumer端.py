# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import pika
user_pwd = pika.PlainCredentials("admin", '123456')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.17.136',
                              credentials=user_pwd)
)

channel = connection.channel()
channel.queue_declare(queue='hello1', durable=True)

def callback(ch, method, properties, body):
    print("[x] recived %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(properties)

channel.basic_consume(
    callback,
    queue='hello1')

channel.start_consuming()