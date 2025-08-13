class Solution:
    def removeConsonants(self, s):
        c = ""
        for i in s:
            if i in "aeiouAEIOU":
                c = c+i
        if c:
            return c
        else:
            return "No Vowel"
