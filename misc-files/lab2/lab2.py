def getColumnSums(mat: list[list[float]]):
    colsums = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            colsums[i] += mat[i][j]

    return colsums

if __name__ == '__main__':

    mat = [[1,1,1],[2,2,2],[3,4,5]]
    colsums = getColumnSums(mat)
    print(colsums)