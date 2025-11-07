class Solution:
    def maxPower(self, s: str) -> int:
        c = 1
        d = []
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c = c+1
            else:
                d.append(c)
                c = 1
        d.append(c)
        return max(d)
