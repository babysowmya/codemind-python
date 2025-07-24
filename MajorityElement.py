from collections import Counter
class Solution:
    def majorityElement(self, arr):
        a = Counter(arr)
        for i in arr:
            if a[i]>len(arr)//2:
                return i
        return -1
