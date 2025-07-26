class Solution:
    def findUnion(self,a,b):
        a = set(a)
        b = set(b)
        c = a.union(b)
        return sorted(c)
