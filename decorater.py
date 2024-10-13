import time
#Decorater function

def delay_decorator_function(func):
    def wrapper_func():
        func()
    return wrapper_func

@delay_decorator_function
def say_hello():
    time.sleep(2)
    print("Hello World!")

def say_goodbye():
    print("Bye")

def say_greeting():
    print("How are you")

say_hello()