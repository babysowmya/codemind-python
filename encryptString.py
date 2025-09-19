class Solution:
    def encryptString(self, s):
        c = 1
        d = []
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c = c+1
            else:
                d.append(s[i-1]+str(c))
                c = 1
        d.append(s[-1]+str(c))
        return ''.join(d)[::-1]
