class Solution:
    def twoRepeated(self, n, arr):
        c = {}
        res = []
        for i in arr:
             c[i]=c.get(i,0)+1
             if c[i]==2:
                 res.append(i)
        return res
