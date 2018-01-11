# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import sessionmaker
"""
engine = create_engine("mysql+pymysql://root:123456@192.168.17.136/test",
                       encoding='utf-8', echo=True)
"""
engine = create_engine("mysql+pymysql://root:123456@192.168.17.136/test",
                       encoding='utf-8')

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'  # 表名
    # 字段
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine)

# 创建与数据库会话的session class，注意这里返回的是一个类，不是一个实例
Session_class = sessionmaker(bind=engine)

# 实例化
Session = Session_class()

user_obj = User(name="test03", password="123456")
user_obj2 = User(name="test04", password="123456")
print(user_obj.name, user_obj.password, user_obj.id)
# 打印name和password有值，但是id没有值，因为此时还没有创建对象

# 可以将Session理解为cursor，将要创建的数据对象添加到这个session中，一会统一创建
# 可以一次添加多个
Session.add(user_obj)
Session.add(user_obj2)
print(user_obj.name, user_obj.password, user_obj.id)

# 只有commit了之后，数据才会真正被创建
Session.commit()
print(user_obj.name, user_obj.password, user_obj.id)
