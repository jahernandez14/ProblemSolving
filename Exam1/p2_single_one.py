def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    map = dict()
    result = 0
    for i in range(len(nums)):
        if nums[i] not in map:
            map[nums[i]] = 1
        else:
            map[nums[i]] += 1

        result = min(map, key=map.get)

    return result