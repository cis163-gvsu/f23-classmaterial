# 2D Recusrion Tracing
Consider the following code:
```
import numpy as np
def mystery(grid):
    return mystery2(grid, 0)
    
def mystery2(grid,i):
    if i == len(grid)-1:
        return mystery3(grid, np.inf, 0, i, 0)
    a, b = mystery2(grid,i+1)
    return mystery3(grid, a, b, i, 0)

def mystery3(grid, cur, c, i, j):
    if j == len(grid[i])-1:
        if grid[i][j] > cur:
            return cur, c
        elif grid[i][j] == cur:
            return cur, c+1
        else:
            return grid[i][j], 1
    a, b = mystery3(grid, cur, c, i, j+1)
    if grid[i][j] > a:
        return a, b
    elif grid[i][j] == a:
        return a, b+1
    else:
        return grid[i][j], 1

grid = [[-8,5,7,1],
        [5,6,-1,6],
        [-3,-3,0,9],
        [-2,-5,-8,-5]]

print(mystery(grid))
```

### Part 1
What is the output of this code?

<br><br><br>

### Part 2
How many times does each function get called?

<br><br><br><br>

What if the grid had been a different size?

<br><br><br><br>

### Part 3
What does this code do?
<br><br><br><br>
