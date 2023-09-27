def sum_elements(lst):
    total = 0
    for x in lst:
        total += x
    return total

def ser(lst):
    print(f'called ser({lst})')
    
    if len(lst) == 1:
        print(f'in base case, returning {lst[0]}')
        return lst[0]

    val =  lst[0] + ser(lst[1:])
    print(f'returning {val}')
    return val

def sersplit(lst):
    n = len(lst)
    if n == 1:
        return lst[0]
    '''
    # could have had base case be list of size 2 rather than 1
    if n == 2:
        return lst[0] + lst[1]
    '''
    return  sersplit(lst[n//2:]) + sersplit(lst[:n//2])

print(sersplit([3,2,1,4]))
