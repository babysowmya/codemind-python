from collections import Counter
class Solution:
    def findTwoElement(self, arr):
        a = Counter(arr)
        c = 0
        d = 0
        for i in range(1,len(arr)+1):
            if a[i]==2:
                c=i
            elif a[i]==0:
                d=i
        return [c,d]
