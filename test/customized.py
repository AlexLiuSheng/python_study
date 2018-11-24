import types


class Custom(object):
    def __init__(self, value) -> None:
        self.value = value
        self.index = 0

    def __str__(self) -> str:
        return 'value:%s' % self.value

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 1
        if self.index > self.value:
            raise StopIteration()
        return self.index

    def __getitem__(self, item):
        return item + 1

    def __getattr__(self, item):
        if item == 'key':
            return 'name'
        raise AttributeError('no attr')

    def __call__(self, *args, **kwargs):
        print("call")


instance = Custom(8)
for n in instance:
    print(n)

print(instance[2])
print(instance.key)
instance()
print(callable(instance))


# print(Custom(8).hehe)

class Chain(object):
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return lambda x, *y: Chain('%s/%s/%s' % (self.__path, path, x))

    def __str__(self):
        return self.__path


print(Chain().users('2'))
