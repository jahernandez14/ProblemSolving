def majority_element(nums):
    """

    :type nums: List[int]
    :rtype: int
    """
    result = 0
    map = dict()
    for i in range(len(nums)):
        if nums[i] not in map:
            map[nums[i]] = 1
        else:
            map[nums[i]] += 1
    result = max(map, key=map.get)
    return result
