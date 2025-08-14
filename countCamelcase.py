class Solution:
    def countCamelCase (self,s):
        c = 0
        for i in s:
            if ord(i)>=65 and ord(i)<=90:
                c = c+1
        return c
