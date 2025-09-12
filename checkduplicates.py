from collections import Counter
class Solution:
    def checkDuplicates(self, arr):
        a = Counter(arr)
        for i in a:
            if a[i]>1:
                return True
        return False
