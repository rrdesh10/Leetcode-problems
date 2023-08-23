def setZeroes(matrix: list[list[int]]):
    m = len(matrix)
    n = len(matrix[0])
    arr = []

    for i in range(m):
        for j in range(n):
                if matrix[i][j] == 0:
                     arr.append([i, j])

    for k, l in arr:
        for row in range(n):
            matrix[k][row] = 0
        for col in range(m):
            matrix[col][l] = 0


m = [[1,2,3],[4,0,5],[6,7,8]]

setZeroes(matrix=m)