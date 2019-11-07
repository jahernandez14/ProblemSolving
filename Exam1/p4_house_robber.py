def house_robber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)

    if n == 0:
        return 0

    value1 = nums[0]
    if n == 1:
        return value1

    value2 = max(nums[0], nums[1])
    if n == 2:
        return value2

    result = None

    for i in range(2, n):
        result = max(nums[i] + value1, value2)
        value1 = value2
        value2 = result

    return result
