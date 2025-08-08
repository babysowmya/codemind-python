class Solution:
    def findExtra(self,a,b):
        res = list(set(a)^set(b))
        if res[0] in a:
            return a.index(res[0])
        else:
            return b.index(res[0])
