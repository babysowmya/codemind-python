class Solution:
    def maxOdd(self, s):
        c = []
        for i in range(len(s)):
            if int(s[i])%2!=0:
                c.append(s[:i+1])
        if c:
            return max(c)
        else:
            return ""
