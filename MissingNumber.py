class Solution:
    def missingNumber(self, arr):
        for i in range(1,max(arr)+2):
            if i not in arr:
                return i
        return 1
