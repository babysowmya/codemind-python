from collections import Counter
class Solution:
    def findDuplicate(self,arr):
        a=Counter(arr)
        for i in set(arr):
            if a[i]>1:
                return i
