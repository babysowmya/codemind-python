class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = 1
        b = 0
        while(n>0):
            r = n%10
            a = a*r
            b = b+r
            n = n//10
        return a-b
