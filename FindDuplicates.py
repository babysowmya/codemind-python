from collections import Counter
class Solution:
    def findDuplicates(self, arr):
        c  = []
        a = Counter(arr)
        for i in a:
            if a[i]!=1:
                c.append(i)
        return c
