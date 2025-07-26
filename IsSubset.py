from collections import Counter
class Solution:
    def isSubset(self, a, b):
        c = 0
        e = Counter(a)
        d = Counter(b)
        for j in b:
            if d[j] > e.get(j,0):
                return False
        return True
