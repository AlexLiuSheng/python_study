def fn(self):
    print("hello")


Hello = type('Hello', (object,), {'hello': fn})

instance = Hello()

instance.hello()
