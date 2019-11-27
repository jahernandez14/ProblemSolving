def stoneGame(piles):
    size = len(piles)

    def dynamicCmp(i, j):
        if i > j: return 0
        same = (j - i - size) % 2
        if same == 1:
            return max(piles[i] + dynamicCmp(i + 1, j), piles[j] + dynamicCmp(i, j - 1))
        else:
            return min(-piles[i] + dynamicCmp(i + 1, j), -piles[j] + dynamicCmp(i, j - 1))

    return dynamicCmp(0, size - 1) > 0


print((stoneGame([1, 2, 3, 1])))
