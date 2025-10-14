from collections import Counter
class Solution:
    def countOccurence(self,arr, k):
        a = Counter(arr)
        b = len(arr)
        c = 0
        for i in a:
            if a[i]>b/k:
                c = c+1
        return c
