from collections import Counter
class Solution:
    def RedOrGreen(self,N,S):
        a = Counter(S)
        b = list(a.values())
        if N==min(b):
            return 0
        else:
            return min(b)
