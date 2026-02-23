class Solution:
    def modify(self, s):
        c = ""
        for i in s:
            if i in "aeiouAEIOU":
                c = c+i
        c = c[::-1]
        s = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                s[i] = c[j]
                j = j+1
        return ''.join(s)
