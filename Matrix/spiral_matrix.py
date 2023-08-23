def spiralMatrix(matrix: list[list[int]]) -> list[int]:

    left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
    res = []

    while left <= right and top <= bottom:

        for i in range(left, right+1):
            res.append(matrix[top][i])
        top += 1
        
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1

        if left > right or top > bottom:
            break

        for i in range(right, left-1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1
        
        for i in range(bottom, top-1, -1):
            res.append(matrix[i][left])
        left += 1

    return res

spiralMatrix([[1,2,3],[4,5,6],[7,8,9]])

        
