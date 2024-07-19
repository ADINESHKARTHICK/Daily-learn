def luckyNumbers(matrix):
    N = len(matrix)
    M = len(matrix[0])
    rowMin = [min(row) for row in matrix]
    colMax = [max(col) for col in zip(*matrix)]
    luckyNumbers = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                luckyNumbers.append(matrix[i][j])
    return luckyNumbers
