class Solution:
    def colSum(self, mat):
        c = []
        for j in zip(*mat):
               c.append(sum(j))
        return c
