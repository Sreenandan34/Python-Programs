#Create a Calculator function using Nested Function
def calc():
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    op=input("operator:")
    def add():
        return a+b
    def sub():
        return a-b
    def div():
        return a/b
    def mul():
        return a*b
    def mod():
        return a%b
    if op=='+':
        print(add())
    elif op=='-':
        print(sub())
    elif op=='/':
        print(div())
    elif op=='*':
        print(mul())
    elif op=='%':
        print(mod())
    else:
        print("Wrong choice")