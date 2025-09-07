from collections import Counter
class Solution:
    def repeatingCharacter(self,s):
        b = list(s)
        a = Counter(s)
        for i in b:
            if a[i]>1:
                return b.index(i)
                break
        return -1
