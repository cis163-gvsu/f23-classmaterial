def longest(lst, cur_max):
    if len(lst) == 0:
        return 0
    if lst[0] > cur_max:
        # choose this element
        opt1 = longest(lst[1:], lst[0])
        # don't choose this element
        opt2 = longest(lst[1:], cur_max)

        return max(opt1+1, opt2)
    else:
        return longest(lst[1:], cur_max)

def longest_increasing(lst):
    return longest(lst, 0)

lst = [3,1,2,6,8,7,15,11,10,12,4,20]
print(longest_increasing(lst))

