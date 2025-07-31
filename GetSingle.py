from collections import Counter
class Solution:
    def getSingle(self,arr):
        a = Counter(arr)
        for i in arr:
            if a[i]%2!=0:
                return i
