class Solution:
    def minDiff(self, arr):
        arr = sorted(arr)
        c = []
        for i in range(len(arr)-1):
            c.append(abs(arr[i]-arr[i+1]))
        return min(c)
