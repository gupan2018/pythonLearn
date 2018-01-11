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

engine = create_engine("mysql+pymysql://root:123456@192.168.17.136/sqlalchemytest",
                       encoding='utf-8',
                       #echo=True
                       )
Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
session = Session_class()


# 插入数据
# b1 = Book(name="BOOK1", pub_date="2014-05-02")
# b2 = Book(name="BOOK2", pub_date="2015-05-02")
# b3 = Book(name="BOOK3", pub_date="2016-05-02")
#
# a1 = Author(name="test01")
# a2 = Author(name="test02")
# a3 = Author(name="test03")
#
# b1.authors = [a1, a3]
# b3.authors = [a1, a2, a3]
#
# session.add_all([b1, b2, b3, a1, a2, a3])
# session.commit()

# 查询数据
author_obj = session.query(Author).filter(Author.name=="test01").first()
print(author_obj.books)
print(author_obj.books[0].pub_date)

book_obj = session.query(Book).filter(Book.id==2).first()
print(book_obj.authors)

# 删除数据：从一本书中删除一名作者，会根据外键关联删除对应项
# book_obj.authors.remove(author_obj)
# session.commit()

# 删除作者,删除时，外键关联关系一并删除
session.delete(author_obj)
session.commit()