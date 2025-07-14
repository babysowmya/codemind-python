class Solution:
    def getAlternates(self, arr):
        c = []
        for i in range(0,len(arr),2):
             c.append(arr[i])
        return c
