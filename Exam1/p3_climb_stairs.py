def climb_stairs(n):
    """
    :type n: int
    :rtype: int
    """
    result = 0
    i=0
    arr = []
    while i <= n:
        if i == 0:
            arr.append(1)
        if i == 1:
            arr.append(1)
        if i > 1:
            arr.append(arr[i - 2] + arr[i - 1])
        i += 1
    result = arr[n]

    return result