def valid(func):
    def inner():
        user=input("user:")
        psd=input("password:")

        if user=='root' and psd=='12345':
            result=func()
            return result
        else:
            return "incorrect username or password"
    return inner

@valid
def secure_file():
    return "secure file"
f=secure_file()
print(f)