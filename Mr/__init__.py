import os
import time


def Meeseeks(func):

    def wrapped(*args, **kwargs):
        while True:
            print('\033[94mI\'m  Mr. Meeseeks! Look at me!')
            try:
                return func(*args, **kwargs)
            except Exception:
                print('Could you help me run {}?'.format(func.__name__))
                time.sleep(2)
                os.fork()

    return wrapped
