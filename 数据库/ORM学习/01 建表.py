# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("mysql+pymysql://root:123456@192.168.17.136/test",
                       encoding='utf-8', echo=True)

# echo=True，打印创建过程的详细信息

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    # 字段
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

# 创建表结构
    # 一旦调用metadata.create_all(engine)就会实例化继承自Base的子类
Base.metadata.create_all(engine)

# 创建表的时候如果没有这张表，就会创建这张表，如果有，不创建

