def repeat(x):
    def dec(func):
        def inner():
            for i in range(x):
                func()
        return inner
    return dec
@repeat(7)
def hello():
    print("hello")
hello()