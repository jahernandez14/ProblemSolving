#################################################################
#################################################################
# 1 twoSum

def twoSum():
    nums = [2, 7, 11, 15]
    numSet = addToSet(nums)

    target = 9
    ans = []
    for i in range(len(nums)):
        if target - nums[i] in numSet:
            ans.append(i)
    print(ans)


#################################################################
#################################################################
# 2 Repeated Numbers

def repeat():
    nums = [3, 4, 6, 1, 3, 10, -1]
    numSet = set()
    for i in nums:
        if i in numSet:
            print(i)
        numSet.add(i)


#################################################################
#################################################################
# 3 Most Common Words

def common():
    str = "hello hi hello hello ten hello"
    arr = str.split(" ")
    map = dict()

    for i in arr:
        if i not in map:
            add = {i: 1}
            map.update(add)
        else:
            map[i] += 1
    maximum = max(map, key=map.get)
    print(maximum)


#################################################################
#################################################################
# 3 Single Number

def single():
    nums = [4, 1, 2, 1, 2]
    map = dict()

    for i in nums:
        if i not in map:
            add = {i: 1}
            map.update(add)
        else:
            map[i] += 1
    maximum = min(map, key=map.get)
    print(maximum)

#################################################################
#################################################################
# 5 Keyboard Problem

def hashKeyboard(word):
    top = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
    middle = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
    bottom = {"z", "x", "c", "v", "b", "n", "m"}

    if word[0] in top:
        for a in word:
            if a not in top:
                return False
    if word[0] in middle:
        for b in word:
            if b not in middle:
                return False
    if word[0] in bottom:
        for c in word:
            if c not in bottom:
                return False
    return True


def keyboard():
    ans = []
    arr = ["hello", "alaska", "dad", "peace"]
    for i in arr:
        result = hashKeyboard(i)
        if result is True:
            ans.append(i)
    print(ans)


#################################################################
# 6 Word Differences
def addToSet(obj):
    hashSet = set()
    for i in obj:
        hashSet.add(i)
    return hashSet


def wordDifferences():
    word1 = "abcde"
    word2 = "abcd"
    set1 = addToSet(word1)
    set2 = addToSet(word2)
    print(set1.difference(set2))

###############################################################


# keyboard()
# wordDifferences()
# twoSum()
# repeat()
# common()
#single()
