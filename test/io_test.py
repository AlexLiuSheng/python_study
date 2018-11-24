from io import StringIO

filePath2 = '/Users/a/AndroidStuidoProjects/cqtravel_merchant/app/release/output.json'
filePath = '/Users/a/AndroidStuidoProjects/cqtravel_merchant/app/release/爱重庆商户端.apk'
filePath3 = '/Users/a/AndroidStuidoProjects/cqtravel_merchant/app/release/python_create.txt'
with open(filePath2, 'r', encoding='gbk') as f:
    for line in f.readlines():
        print(line.strip())

with open(filePath3, 'w', encoding='utf-8') as f:
    f.write('hello python,I am allen')


# StringIO 内存中读写str

def read():
    io = StringIO("read from io")
    while True:
        string = io.readline()
        if string == '':
            break
        print(string.strip())


def write(text):
    io = StringIO()
    io.write(text)
    print(io.getvalue())


read()
write("write io")

#BytesIO
