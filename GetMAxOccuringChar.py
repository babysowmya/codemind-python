from collections import Counter
class Solution:
    def getMaxOccurringChar(self, s):
        a = Counter(s)
        c = max(a.values())
        d = []
        for i in a:
            if a[i]==c:
                d.append(i)
        return min(d)
