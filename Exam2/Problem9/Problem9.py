def numSquares(n):
    dp = [i for i in range(0, n + 1)]
    squareLen = int(n ** 0.5)
    for i in range(2, squareLen + 1):
        curSquare = i ** 2
        for j in range(curSquare, n + 1):
            dp[j] = min(dp[j], 1 + dp[j - curSquare])
    return dp[n]


print(numSquares(12))
