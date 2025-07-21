class Solution:
    def missingNum(self, arr):
        a = min(arr)
        b = max(arr)
        c = set(arr)
        for i in range(1,b):
            if i not in c:
                return i
        return b+1
