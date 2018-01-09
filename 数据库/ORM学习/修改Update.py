# -*- coding:utf-8 -*-
# __author__ = 'gupan'
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@192.168.17.136/test",
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

Session_class = sessionmaker(bind=engine)
Session = Session_class()

# 修改一行数据
'''
data = Session.query(User).filter(User.id > 1).filter(User.id < 3).first()
print(data)
data.name = "gupan"
data.password = "qwer"
Session.commit()
'''

# 修改多行数据（进行批量修改）