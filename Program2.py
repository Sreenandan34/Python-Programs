def Dec(func):
    def inner(x, y):
        print(x, y)
        print(x + y)
        func(x, y)
    return inner


@Dec
def fun2(a, b):
    print("Inside fun2")


fun2(200, 0.5)

print("ending this function")