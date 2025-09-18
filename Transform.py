from collections import Counter
class Solution:
    def transform(self, s):
        s = s.lower()
        c = 1
        d = ""
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c = c+1
            else:
                d = d+str(c)+s[i-1]
                c = 1
        d = d+str(c)+s[-1]
        return d
