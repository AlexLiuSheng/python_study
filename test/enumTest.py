from enum import Enum, unique

# index 默认从1开始
Numer = Enum('NUMBER', ('ONE', 'TWO', 'THREE'))

for name, member in Numer.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Number2(Enum):
    ONE = 0
    TWO = 1
    THREE = 3


print(Number2.ONE.value)
