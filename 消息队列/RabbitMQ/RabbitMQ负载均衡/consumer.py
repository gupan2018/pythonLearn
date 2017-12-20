# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import pika
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        'localhost'
    )
)

channel = connection.channel()
channel.queue_declare(queue='queue_test1', durable=True)
def callback(ch, method, properties, body):
    print("received msg:", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 在客户端加上这一句话即可实现负载均衡的模式
channel.basic_qos(prefetch_count=1)

consume = channel.basic_consume(
    callback,
    queue='queue_test1',
    no_ack=False)
channel.start_consuming()
