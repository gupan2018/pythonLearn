# -*- coding:utf-8 -*-
# __author__ = 'gupan'
name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

info = '''------info of %s-------
Age:%s
Job:%s
Salary:%s
'''%(name, age, job, salary)
#print(info)

info2 = '''--------info2 of {_name}-------
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)

info3 = '''------info of {0}-----
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)
print(info3)

