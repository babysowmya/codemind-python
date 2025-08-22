class Solution:
    def removeSpecialCharacter (self, S):
        c = ""
        for i in S:
            if i.isalpha():
                c = c+i
        if c:
            return c
        else:
            return -1
