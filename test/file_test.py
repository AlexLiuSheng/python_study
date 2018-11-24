import os

print(os.name)
print(os.environ)

basePath = os.path.abspath('.')
path = os.path.join(basePath, 'python_create_file_test')
file = os.path.join(path, 'test.txt')
# os.mkdir(path)
# os.rmdir(path)
print(os.path.split(file))
print(os.path.splitext(file))

renamePath = '/Users/a/AndroidStuidoProjects/cqtravel_merchant/app/release/爱重庆商户端.apk'
p = os.path.split(renamePath)[0]
oldName = os.path.split(renamePath)[1]
newName = 'python.apk'
os.rename(os.path.join(p + '/' + oldName), os.path.join(p + '/' + newName))
