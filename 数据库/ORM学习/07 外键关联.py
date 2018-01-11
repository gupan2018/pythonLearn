# -*- coding:utf-8 -*-
# __author__ = 'gupan'
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# engine = create_engine("mysql+pymysql://root:123456@192.168.17.136/sqlalchemytest",
#                        encoding="utf-8",
#                        echo=True
#                        )

engine = create_engine("mysql+pymysql://root:123456@192.168.17.136/sqlalchemytest",
                       encoding="utf-8"
                       )

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "id:%s name:%s register_date:%s" % (self.id, self.name, self.register_date)

class StudyRecord(Base):
    __tablename__ = "studyrecord"
    id =Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)

    # 创建外键
    stu_id = Column(Integer, ForeignKey("student.id"))

    # 可以在StudyRecord中通过student字段反查Student表，
    # 在Student表中通过my_study_record字段反查StudyRecord表
    student = relationship("Student", backref="my_study_record")
    def __repr__(self):
        return "stu_name : {id}, day:{day}, status:{status} ".format(id=self.student.name,
                                                               day=self.day,
                                                               status=self.status)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()

# 创建表数据
# s1 = Student(name="test01", register_date="2014-05-21")
# s2 = Student(name="test02", register_date="2015-05-21")
# s3 = Student(name="test03", register_date="2016-05-21")
# s4 = Student(name="test04", register_date="2017-05-21")
#
# study_obj1 = StudyRecord(day=1, status="YES", stu_id=1)
# study_obj2 = StudyRecord(day=2, status="NO", stu_id=1)
# study_obj3 = StudyRecord(day=3, status="YES", stu_id=1)
# study_obj4 = StudyRecord(day=1, status="YES", stu_id=1)
# study_obj5 = StudyRecord(day=1, status="YES", stu_id=2)
# Session.add_all([s1, s2, s3, s4,
#                  study_obj1, study_obj2, study_obj3, study_obj4, study_obj5])
# Session.commit()

# 连接查询
# data = Session.query(Student).join(StudyRecord).all()

student = Session.query(Student).filter(Student.id==1).first()
print(student.my_study_record)