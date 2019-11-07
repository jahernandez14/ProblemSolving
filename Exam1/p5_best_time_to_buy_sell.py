def best_time(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min = max(prices)
    result = 0
    
    for i in prices:
        if i < min:
            min = i
        if i - min > result:
            result = i - min

    return result