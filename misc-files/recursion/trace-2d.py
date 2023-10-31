import numpy as np
def mystery(grid):
    return mystery2(grid, np.inf, 0, 0)
    
def mystery2(grid, cur, c,  i):
    if i == len(grid)-1:
        return mystery3(grid, cur, c, i, 0)
    a, b = mystery2(grid, cur, c,i+1)
    if a > cur:
        return mystery3(grid, cur, c, i, 0)
    elif a == cur:
        return mystery3(grid, cur+1, c+1, i, 0)
    else:
        return mystery3(grid, a, b, i, 0)

def mystery3(grid, cur, c, i, j):
    if j == len(grid[i])-1:
        return grid[i][j], 1
    a, b = mystery3(grid, cur, c, i, j+1)
    if a > cur:
        return cur, c
    elif a == cur:
        return cur, c+1
    else:
        return a, b

grid = [[1,5,7,1],
        [5,6,-1,6],
        [-3,-3,0,9],
        [-2,-5,1,9]]

print(mystery(grid))

