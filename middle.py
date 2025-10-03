class Solution:
    def middle(self, a, b, c):
        res = []
        res.append(a)
        res.append(b)
        res.append(c)
        res = sorted(res)
        return res[1]
