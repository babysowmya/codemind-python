from collections import Counter
class Solution:
    def isIsogram(self,s):
        a = Counter(s)
        for I in a:
            if a[I]>1:
                return False
        return True
