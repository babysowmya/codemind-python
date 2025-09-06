class Solution:
    def maxAdj(self, arr):
        c = []
        for I in range(len(arr)-1):
            if arr[I]>arr[I+1]:
                c.append(arr[I])
            else:
                c.append(arr[I+1])
        return c
