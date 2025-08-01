from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        f = False
        c = []
        a = Counter(arr)
        for i in set(arr):
            if i==a[i]:
                c.append(i)
                f = True
        if f:
            return max(c)
        return -1
