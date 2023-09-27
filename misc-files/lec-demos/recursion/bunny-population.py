def piterative(n):
    lst = []
    for i in range(n):
        if i == 0 or i == 1:
            lst.append(1)
        else:
            lst.append(lst[i-1] + lst[i-2])
    return lst

def precursive(n):
    # base case
    if n == 1:
        return 1
    if n == 2:
        return 1
    # recursive case
    return precursive(n-1) + precursive(n-2)

print(precrusive(6))
print(piterative(6))

