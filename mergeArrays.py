class Solution:
    def mergeArrays(self, a, b):
        z = a+b
        c = sorted(z)
        d = c[:len(a)]
        e = c[len(a):]
        a[:]=d
        b[:]=e
        return a,b
