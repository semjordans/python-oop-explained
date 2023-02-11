def myDeco(func):
    def wrapper():
        print("hello decorator")
        func()
        print("Done!")

    return wrapper


def helloDeco():
    print("Yes there !!")


hello = myDeco(helloDeco)

hello()