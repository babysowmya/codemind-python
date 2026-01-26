class Solution:
    def solve(self, n, d):
        c = []
        for i in range(n+1):
            if str(d) in str(i):
                c.append(i)
        if c:
            return c
        else:
            c.append(-1)
            return c
