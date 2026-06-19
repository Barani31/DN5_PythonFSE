def decorator(func):
    
    def wrapper():
        print("Before Function")
        func()
        print("After Function")

    return wrapper

@decorator
def hello():
    print("Hello")

hello()