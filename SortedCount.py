class Solution:
    def sortedCount(self,N,M,Mat):
        c = 0
        for i in Mat:
            inc = True
            for j in range(M-1):
                if i[j]>=i[j+1]:
                    inc = False
                    break
            dec = True
            for j in range(M-1):
                if i[j]<=i[j+1]:
                    dec = False
                    break
            if inc or dec:
                c = c+1
        return c
