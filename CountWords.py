from collections import Counter
class Solution:
    def countWords(self,List, n):
        c = 0
        a = Counter(List)
        for i in a:
            if a[i]==2:
                c = c+1
        return c
