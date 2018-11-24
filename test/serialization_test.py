import json
import os
import pickle

d = dict(name='allenliu', age=15, gender='男')
# binrary
print(pickle.dumps(d))
# file
p = os.path.join(os.path.abspath('.'), 'binrary.txt')
# os.makedirs(p)
f = open(p, 'wb+')
pickle.dump(d, f)

# json
j = os.path.join(os.path.abspath('.'), 'json.txt')
f2 = open(j, 'w+')
json.dump(d, f2)
print(json.dumps(d))


class Student(object):
    def __init__(self, name):
        self.name = name


def std2dict(p):
    return dict(name=p.name)


def dict2std(p):
    return Student(p['name'])


print(json.dumps(Student('你好'), default=std2dict))
print(json.dumps(Student('nihao '), default=lambda obj: obj.__dict__))

demo_str = '{"name": "帅哥啊 "}'
print(json.loads(demo_str, object_hook=dict2std))
