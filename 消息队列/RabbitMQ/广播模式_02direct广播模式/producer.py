# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import sys
import pika

severity_list = ['warning', 'error', 'info']

user_pwd = pika.PlainCredentials("admin", '123456')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.17.136',
                              credentials=user_pwd)
)

channel = connection.channel()
channel.exchange_declare(
    exchange="logs_02",
    exchange_type="direct"
)

severity = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in severity_list else 'info'
msg = "".join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(
    exchange='logs_02',
    # 在direct模式下，routing_key参数需要填写
    routing_key=severity,
    body=msg
)


print(" [x] Sent %r:%r" % (severity, msg))
connection.close()
