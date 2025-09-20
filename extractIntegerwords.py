class Solution:
    def extractIntegerWords(self, s):
        d = []
        c = ""
        for i in range(len(s)):
            if s[i].isdigit():
                c = c+s[i]
                if i==len(s)-1 or not s[i+1].isdigit():
                    d.append(c)
                    c = ""
        return d
