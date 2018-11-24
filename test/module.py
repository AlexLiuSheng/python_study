import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("hello module")
    elif len(args) == 2:
        print('params:', args[1])

    else:
        print("too many params")


if __name__ == '__main__':
    test()
