class Solution:
    def findMinSum(self, A,B,N):
        c = 0
        a = sorted(A)
        b = sorted(B)
        for i in range(len(a)):
            c = c+abs(a[i]-b[i])
        return c
