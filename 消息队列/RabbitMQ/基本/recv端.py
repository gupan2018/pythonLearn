# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import pika
connection = pika.BlockingConnection(
    pika.ConnectionParamters('localhost')
)

channel = connection.channel()

# 声明收消息的队列
channel.queue_declare(queue='hello')

# 标准格式就带四个参数
def callback(ch, method, properities, body):
    # ch：管道的内存对象地址
    # method：消息发给谁，发给哪些队列之类的信息
    # properties:
    print("[x] recived %r" % body)
    # 发送确认消息，对应channel.basic_consume中的no_ack参数
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 消费消息，只是声明了收到消息后要进行的处理，在调用start_consuming才开始收消息
channel.basic_consum(
    # 如果收到消息，就调callback函数来处理消息
    callback,
    # 要从那个队列中收消息
        # 在send端已经申明了hello这个队列，如果你确定send端已经声明了这个队列，
        # 那么可以不声明这个队列，但在实际过程中，并不确定send端还是recv端先运行
        # 如果recv端先运行，并且没有声明接收队列，那么程序会报错
    queue='hello',
    #
    no_ack=True)

# 开始收消息，调用start_consuming()这个函数以后，程序会一直运行
channel.start_consuming()