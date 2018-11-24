# pool 进程池
import os
from multiprocessing.pool import Pool


def child_pool_process(name):
    print("current process name:%s and pid is %s" % (name, os.getpid()))


if __name__ == '__main__':
    print("parent process start")
    pool = Pool(4)
    for i in range(4):
        pool.apply_async(child_pool_process, ("param",))
    print("waiting for all child process finish")
    pool.close()
    pool.join()
    print("all done")
