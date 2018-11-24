import os

print(" process start,process id %s" % (os.getpid()))

f = os.fork()
if f == 0:
    print("current is child process ")
else:
    print("current is parent process . id is %s" % (f,))
