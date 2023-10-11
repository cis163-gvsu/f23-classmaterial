import math

'''
def foo(x):
    try:
        return math.sqrt(x)
    except ValueError:
        return x
'''
def foo(x):
    return math.sqrt(x)


z = 'cat'
try:
    y = foo(z)
except ValueError:
    print(z)
except TypeError:
    print('invalid')
else:
    # no exception occurred
    print(y)
finally:
    print('done')


