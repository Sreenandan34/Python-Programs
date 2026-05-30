def Dec(func):
    def inner(x,y):
        if isinstance(x,int) and isinstance(y,int):
            print("sending integers")
        elif isinstance(x,str) and isinstance(y,str):
            print("sending strings")
            func(x,y)
        else:
            print("invalid inputs")
    return inner
@Dec
def fun2(a,b):
    print(str(a)+str(b))
fun2("hello","hi")