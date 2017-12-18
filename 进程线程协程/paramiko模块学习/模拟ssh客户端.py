# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import paramiko

# 创建ssh对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname="192.168.17.131", port=22, username="root", password="free930923")

# 执行命令
stdin, stdout, stderr = ssh.exec_command("df")

result = None

# 执行命令结果
# 执行命令结果
res, err = stdout.read(), stderr.read()
result = res if res else err
print(result)