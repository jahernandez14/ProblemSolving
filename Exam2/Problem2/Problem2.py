def minFallingPathSum(A):
    while len(A) >= 2:
        row = A.pop()
        for i in range(len(row)):
            A[-1][i] += min(row[max(0, i - 1): min(len(row), i + 2)])
    return min(A[-1])


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(A[-1][0])
print(minFallingPathSum(A))

