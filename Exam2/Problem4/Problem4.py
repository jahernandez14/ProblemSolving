def numberOfArithmeticSlices(A):
    N = len(A)
    dp = [0] * N
    for i in range(1, N - 1):
        if A[i - 1] + A[i + 1] == A[i] * 2:
            dp[i] = dp[i - 1] + 1
    return sum(dp)

print(numberOfArithmeticSlices([1,2,3,4]))