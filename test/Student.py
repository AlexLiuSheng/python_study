import types


class Student(object):

    def __init__(self, name, score, password='1'):
        self.name = name
        self.password = password
        self.__score = score

    def hehe(self):
        pass

    def __len__(self):
        return 100

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


instance = Student('hehe', 2)
instance.score = 12
instance.testProperty = 'add property'

print(type(instance))
print(type(instance.hehe) == types.BuiltinFunctionType)
print(len(instance))

setattr(instance, 'password', 20)
print(instance.password)
print(instance.score)
print(hasattr(instance, 'getScore'))
print(instance.testProperty)


def add_method(self, index):
    print('add method', index)


#
# 给实例增加方法


instance.add_method = types.MethodType(add_method, instance)

instance.add_method(1)

# 直接给类帮顶方法
Student.add_method = add_method
instance.add_method(2)


# __slots__
class Student2(object):
    __slots__ = ('age', 'name', 'value')

    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return 'string:%s' % self.value


s2 = Student2('heh')
print(s2)
