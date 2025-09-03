class Solution:
    def rowWithMax1s(self, arr):
        d = []
        for i in arr:
            c = 0
            for j in i:
                if j==1:
                     c = c+1
            d.append(c)
        a = max(d)
        e = d.index(a)
        return e
