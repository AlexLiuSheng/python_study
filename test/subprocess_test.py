import subprocess
from multiprocessing import Queue, Process

sub = subprocess.call(['ping', '-c', '5', 'www.python.org'])

print('Exit code:', sub)


#  输入 communicate

# Queee

def read(q):
    while True:
        print('read value:%s' % q.get(True))


def write(q):
    for x in ('a', 'b', 'c'):
        q.put(x)


def start():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

start()
