# coding: utf-8
def foo(x):
    return x
    
get_ipython().run_line_magic('clear', '')
get_ipython().run_line_magic('clear', '')
get_ipython().run_line_magic('clear', '')
def combine(first, middle, last):
    return first + ' ' + middle + ' ' + last
    
combine('Bob', 'Middle', 'Smith')
def combine(first, last, middle=''):
    if len(middle) == 0:
        return first + ' ' + last
    else:
        return first + ' ' + middle + ' ' + last
        
combine('Bob', 'Smith', 'Middle')
combine('Bob', 'Smith')
combine('Bob', 'Smith', middle='Middle')
combine(last='Smith', first='Bob', middle='M.')
combine('Smith', 'Bob', 'M.')
