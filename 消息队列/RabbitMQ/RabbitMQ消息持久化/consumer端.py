# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import pika
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()
channel.queue_declare(queue='hello1', durable=True)

def callback(ch, method, properities, body):
    print("[x] recived %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    callback,
    queue='hello1')

channel.start_consuming()