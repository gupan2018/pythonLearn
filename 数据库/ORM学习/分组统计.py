# -*- coding:utf-8 -*-
# __author__ = 'gupan'
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@192.168.17.136:3306/test",
                       encoding="utf-8"
                       )

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "id:%s name:%s password:%s" % (self.id, self.name, self.password)
Base.metadata.create_all(engine)
#
Session_class = sessionmaker(bind=engine)
Session = Session_class()

# sqlalchemy模糊查询
# 统计
from sqlalchemy import and_
count_01 = Session.query(User).filter(and_(*[User.name.like(w) for w in ['test%']])).count()
count_02 = Session.query(User).filter(User.name.in_(['test01', 'gupan'])).count()
print(count_02)
# 分组
from sqlalchemy import func
data = Session.query(User.name, func.count(User.name)).group_by(User.name).all()
print(data)