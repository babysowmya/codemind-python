class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = bin(n)[2:]
        c = 1
        for i in range(len(a)-1):
            if a[i]!=a[i+1]:
                c = c+1
        if c==len(a):
            return True
        else:
            return False
