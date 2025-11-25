class Solution:
    def amendSentence(self, s):
        res = ""
        for i in range(len(s)):
            if s[i].isupper() and i!=0:
                res = res+" "
            res = res+s[i].lower()
        return res
