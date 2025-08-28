from collections import Counter
class Solution:
    def solve(self, N):
        a = Counter(N)
        c = []
        b = max(a.values())
        for i in a:
            if a[i]==b:
                c.append(i)
        return max(c)
