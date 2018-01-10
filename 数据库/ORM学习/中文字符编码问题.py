# -*- coding:utf-8 -*-
# __author__ = 'gupan'
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DATE, Table
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# 创建著作和作者之间的关系表
book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

# 对于Book和Author来说，关系表是透明的
# 但是要利用Book和Author表之间的关系，需要secondary这一个字段，指定第三张表
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name
# 如果要在连接的时候支持中文，需要这样写
engine = create_engine("mysql+pymysql://root:123456@192.168.17.136/sqlalchemytest?charset=utf8",
                       encoding='utf-8',
                       #echo=True
                       )
Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
session = Session_class()


# 插入数据
b1 = Book(name="我的书", pub_date="2014-05-02")

a1 = Author(name="顾攀")

b1.authors = [a1]

session.add_all([b1,a1])

session.commit()