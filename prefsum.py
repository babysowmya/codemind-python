class Solution:
    def prefSum(self, arr):
        d = []
        c = 0
        for i in arr:
            c = c+i
            d.append(c)
        return d
