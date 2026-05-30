import functools
import time
from datetime import datetime


# Decorator using wraps
def Dec(func):
    @functools.wraps(func)
    def Inner():
        func()

    return Inner


@Dec
def fun():
    """this is DocString"""
    print("hello")


print(fun.__doc__)
print(fun.__name__)

# Current date and time
time.sleep(2)
print(datetime.now())
print(time.asctime())


# Timer Decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print("Started:", time.asctime())

        result = func(*args, **kwargs)
        print("Sum:", result)

        end = time.time()
        print("Ended:", time.asctime())
        print("Time taken:", end - start)

    return wrapper


@timer
def add(x, y):
    su = 0
    for i in range(1, x + y + 1):
        su += i
    return su


add(10000, 200000)

print(add.__doc__)
print(time.asctime())
print(list(time.asctime().split()))
