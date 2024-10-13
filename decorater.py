import time
#Decorater function
#
# def delay_decorator_function(func):
#     def wrapper_func():
#         time.sleep(2)
#         #Do something before
#         func()
#         func()
#         #do something after
#     return wrapper_func
#
# @delay_decorator_function
# def say_hello():
#     print("Hello World!")
#
# def say_goodbye():
#     print("Bye")
#
# def say_greeting():
#     print("How are you")
#
# say_greeting()

#other challenge:
import time


def speed_calc_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()