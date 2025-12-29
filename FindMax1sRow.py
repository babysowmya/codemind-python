class Solution:
    def findMax1sRow(self, mat):
        c = []
        for i in mat:
            c.append(i.count(1))
        a = max(c)
        return c.index(a)
