# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import os
import sys

# 未实现：以后实现

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DATE, Table, Enum, UniqueConstraint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import ChoiceType
from conf import settings

Base = declarative_base()
# 废弃表
# host_m2m_userprofile = Table("host_m2m_userprofile", Base.metadata,
#                              Column("host_id", Integer, ForeignKey("host.id")),
#                              Column("user_profile", Integer, ForeignKey("user_profile.id"))
#                              )
#
# host_m2m_remoteuser = Table("host_m2m_remoteuser", Base.metadata,
#                             Column("host_id", Integer, ForeignKey("host.id")),
#                             Column("remoteuser_id", Integer, ForeignKey("remote_user.id"))
#                             )
#
# host_m2m_host_group = Table("host_m2m_hostgroup", Base.metadata,
#                            Column("host_id", Integer, ForeignKey("host.id")),
#                            Column("host_group_id", Integer, ForeignKey("host_group.id"))
#                             )
user_profile_m2m_bind_host = Table("user_profile_m2m_bind_host", Base.metadata,
                                   Column("user_profile_id", Integer, ForeignKey("user_profile.id")),
                                   Column("bind_host_id", Integer, ForeignKey("bind_host.id"))
                                   )

bind_host_m2m_host_group = Table("bind_host_m2m_host_group", Base.metadata,
                                   Column("bind_host_id", Integer, ForeignKey("bind_host.id")),
                                   Column("host_group_id", Integer, ForeignKey("host_group.id"))
                                   )

user_profile_m2m_host_group = Table("user_profile_m2m_host_group", Base.metadata,
                                   Column("user_profile_id", Integer, ForeignKey("user_profile.id")),
                                   Column("host_group_id", Integer, ForeignKey("host_group.id"))
                                   )

class Host(Base):
    __tablename__ = "host"
    __table_args__ = {
                          "mysql_engine":"innodb",
                          "mysql_charset":"utf8"
                      }
    id = Column(Integer, primary_key=True)
    hostname = Column(String(64), unique=True, nullable=False)
    ip = Column(String(16), unique=True, nullable=False)
    port = Column(Integer, default=22, nullable=False)

    def __repr__(self):
        return "{ip}:{port}".format(ip=self.ip, port=self.port)

# 堡垒机账户
class UserProfile(Base):
    __tablename__ = "user_profile"
    id = Column(Integer, primary_key=True)
    __table_args__ = (UniqueConstraint("username", "password", name="_user_passwd"),
                      {
                          "mysql_engine":"innodb",
                          "mysql_charset":"utf8"
                      })
    username = Column(String(64), unique=True)
    password = Column(String(64), nullable=False)
    #hosts = relationship("Host", secondary=host_m2m_userprofile, backref="user_profiles")
    bind_hosts = relationship("BindHost", secondary=user_profile_m2m_bind_host, backref="user_profiles")
    host_groups = relationship("HostGroup", secondary=user_profile_m2m_host_group, backref="user_profiles")

    def __repr__(self):
        return "name:{name}, password:{password}".format(name=self.username, password=self.password)

class RemoteUser(Base):
    __tablename__ = "remote_user"
    # hosts = relationship("Host", secondary=host_m2m_remoteuser, backref="remote_users")
    # 声明联合唯一
    __table_args__ = (UniqueConstraint("auth_type", "username", "password", name="_user_passwd_authtype_uc"),
                      {
                          "mysql_engine": "innodb",
                          "mysql_charset": "utf8"
                      }
                      )
    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False)
    password = Column(String(128))
    AuthTypes = [
        (['ssh-password', 'SSH/Password']),
        (['ssh-key', 'SSH/KEY'])
    ]

    auth_type = Column(ChoiceType(AuthTypes))

    def __repr__(self):
        return "username:{username}, password:{password}".format(username=self.username,
                                                                 password=self.password)
class HostGroup(Base):
    __tablename__ = "host_group"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    __table_args__ = {
                          "mysql_engine":"innodb",
                          "mysql_charset":"utf8"
                      }
    bind_hosts = relationship("BindHost", secondary=bind_host_m2m_host_group, backref="host_groups")
    def __repr__(self):
        return self.name

class BindHost(Base):
    '''
    192.168.17.136  web bj_group
    192.168.17.136  mysql bj_group
    '''
    __tablename__ = "bind_host"
    __table_args__ = (UniqueConstraint("host_id", "remoteuser_id", name="__host_group_remoteuser_uc"),
                      {
                          "mysql_engine": "innodb",
                          "mysql_charset": "utf8"
                      }
                      )
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey("host.id"))
    # group_id = Column(Integer, ForeignKey("group.id"))
    remoteuser_id = Column(Integer, ForeignKey("remote_user.id"))

    host = relationship("Host", backref="bind_hosts")

    remote_user = relationship("RemoteUser", backref="bind_hosts")

    def __repr__(self):
        return "<%s -- %s -- %s>" % (self.host.ip, self.remote_user.username, self.host_groups)



# class AuditLog(Base):
#     __tablename__ = "audit_log"
#     id = Column(Integer, primary_key=True)
#     date = Column(DATE, nullable=False)
#     user = Column(String(64))
#     cmd = Column(String(128))
#     ip = Column(String(16))
#     remote_user = Column(String(64))

# if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)