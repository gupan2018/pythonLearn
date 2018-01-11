# -*- coding:utf-8 -*-
# __author__ = 'gupan'
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    # 不指定foreign_keys字段的值，会报错
    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])

    def __repr__(self):
        return "billing_address:{bill_addr}, shipping_addr:{ship_addr}".format(
            bill_addr=self.billing_address,
            ship_addr=self.shipping_address
        )

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

    def __repr__(self):
        return self.street


engine = create_engine("mysql+pymysql://root:123456@192.168.17.136/sqlalchemytest",
                       encoding="utf-8",
                       #echo=True
                       )
Base.metadata.create_all(engine)

# 注意：以下代码应该在其余模块中进行编写
Session_class = sessionmaker(bind=engine)
session = Session_class()

# 插入数据
# addr1 = Address(street="Shazhengjie", city="Shapinba", state="Chongqing")
# addr2 = Address(street="Datonglu", city="Jiangjin", state="Chongqing")
# addr3 = Address(street="Dishili", city="Pudong", state="Shanghai")
#
# session.add_all([addr1, addr2, addr3])
#
# c1 = Customer(name="test01", billing_address=addr1, shipping_address=addr2)
# c2 = Customer(name="test02", billing_address=addr3, shipping_address=addr3)
# session.add_all([c1, c2])
# session.commit()

obj = session.query(Customer).filter(Customer.name=="test01").all()
print(obj)