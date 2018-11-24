import os
from multiprocessing import Process


def child_process(name):
    print("current process name:%s and pid is %s" % (name, os.getpid()))


if __name__ == '__main__':
    print("parent process start")

    ins = Process(target=child_process, name="child process", args=("params",))

    ins.start()
    print("child process start")
    ins.join()
    print("child process finish")



