class Solution:
    def splitString(ob, S): 
        c = ""
        d = ""
        e = ""
        for i in S:
            if i.isalpha():
                c = c+i
            elif i.isdigit():
                d = d+i
            else:
                e = e+i
        return c,d,e
