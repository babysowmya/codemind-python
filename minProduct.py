class Solution:
    def minProduct(self, arr, k): 
        m = 10**9+7
        k = min(k,len(arr))
        a = sorted(arr)
        c = 1
        for i in range(k):
            c = (c*a[i])%m
        return c
