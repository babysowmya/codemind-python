class Solution:
    def getMoreAndLess(self, arr, target):
        c = 0
        d = 0
        for i in arr:
            if i<=target:
                c = c+1
            if i>=target:
                d = d+1
        return c,d
