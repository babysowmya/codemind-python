class Solution:
    def count (self,s):
        a = b = c = d = 0
        for i in s:
            if ord(i)>=65 and ord(i)<=90:
                a = a+1
            elif ord(i)>=97 and ord(i)<=122:
                b = b+1
            elif ord(i)>=48 and ord(i)<=57:
                c = c+1
            else:
                d = d+1
        return a,b,c,d
