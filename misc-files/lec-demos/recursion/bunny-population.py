def piterative(n):
    lst = []
    for i in range(n):
        if i == 0 or i == 1:
            lst.append(1)
        else:
            lst.append(lst[i-1] + lst[i-2])
    return lst

def precursive(n, prev_results):
    if n in prev_results:
        print(f'called pr({n}) - knew answer')
        return prev_results[n]
    else:
        print(f'called pr({n}) - computing answer')
    # base case
    if n == 1:
        my_result =  1
    elif n == 2:
        my_result = 1
    # recursive case
    else:
        my_result = precursive(n-1, prev_results) + precursive(n-2, prev_results)
    prev_results[n] = my_result
    #print(prev_results)
    return my_result

print(precursive(20, {10:55, 9:34}))
print(piterative(6))

