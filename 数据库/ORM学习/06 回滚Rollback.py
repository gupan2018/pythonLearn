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

user_obj = User(name="test13", password="123456")
Session.add(user_obj)

data = Session.query(User).filter(User.name.in_(["test13", "test01"])).all()
print(data)
Session.rollback()
Session.commit()

# 检测rollback是否生效
data = Session.query(User).filter(User.name.in_(["test13", "test01"])).all()
print(data)