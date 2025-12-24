class Solution:
    def countPairs(self,arr1, arr2, x):
        arr2 = set(arr2)
        c = 0
        for i in arr1:
            if x-i in arr2:
                c = c+1
        return c
