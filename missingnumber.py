class Solution:
    def missingNumber(self, arr):
       a = len(arr)+1
       b = a*(a+1)//2
       return abs(sum(arr)-b)
