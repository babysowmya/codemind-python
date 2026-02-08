class Solution:
    def maxNtype(self , arr):
        a = sorted(arr)
        b = a[::-1]
        
        if arr==a:
            return 1
        if arr==b:
            return 2
        m = b.index(arr[0])
        if b[m:]+b[:m]==arr:
            return 3
        return 4
