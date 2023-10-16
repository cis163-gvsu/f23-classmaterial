import math

class MyException(Exception):
    pass

def foo(x):
    try:
        return math.sqrt(x)
    except ValueError:
        raise MyException('tried calling with bad value')
'''
def foo(x):
    return math.sqrt(x)
'''


z = -1
try:
    y = foo(z)
except ValueError:
    print(z)
except TypeError:
    print('invalid')
except Exception:
    print(e)
    print(type(e))
else:
    # no exception occurred
    print(y)
finally:
    print('done')


