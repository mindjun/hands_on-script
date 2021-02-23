import signal
import time
from functools import wraps


# def handler(signum, frame):
#     raise TimeoutError('TimeoutError')
#
#
# def timeout(seconds=None):
#     def decorate(function):
#         @wraps(function)
#         def new_function(*args, **kwargs):
#             try:
#                 return function(*args, **kwargs)
#             finally:
#                 signal.setitimer(signal.ITIMER_REAL, seconds)
#                 signal.signal(signal.SIGALRM, handler)
#         return new_function
#
#     return decorate

# class TimeOutException(Exception):
#    pass
#
#
# def alarm_handler(signum, frame):
#     print("ALARM signal received")
#     raise TimeOutException()
#
#
# def loop(n):
#     for sec in range(n):
#         print("sec {}".format(sec))
#         time.sleep(1)
#
#
# signal.signal(signal.SIGALRM, alarm_handler)
# signal.alarm(8)
#
#
# def outer():
#     try:
#         loop(6)
#     except TimeOutException as ex:
#         print(ex)
#     signal.alarm(0)
#
#
# def inner():
#     print('start')
#     for i in range(1, 10):
#         time.sleep(i)
#         print("{} seconds have passed".format(i))
#     return []

def raise_timeout(signum, frame):
    raise TimeoutError('timeout error')


def timeout(seconds):
    # Register a function to raise a TimeoutError on the signal.
    signal.signal(signal.SIGALRM, raise_timeout)
    # Schedule the signal to be sent after ``time``.
    signal.alarm(seconds)

    try:
        return my_test()
    except TimeoutError as ex:
        print(ex)
        return 'error'
    finally:
        # Unregister the signal so it won't be triggered
        # if the timeout is not reached.
        signal.signal(signal.SIGALRM, signal.SIG_IGN)


def my_test():
    print('start')
    import random
    t = random.randint(1, 10)
    print(f'sleep {t}')
    time.sleep(t)
    print("{} seconds have passed".format(t))
    return 'my_test'


# timeout(5)


def outer():
    for i in range(10):
        try:
            print(timeout(5))
            print('\n')
        except Exception as ex:
            print(ex)


outer()
