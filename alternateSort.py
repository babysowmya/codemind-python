class Solution:
    def alternateSort(self,arr):
        n = len(arr)//2
        a = sorted(arr)
        x = a[:n]
        y = a[n:][::-1]
        c = []
        for i in range(n):
            c.append(y[i])
            c.append(x[i])
        if len(arr)%2==0:
            return c
        elif len(x)>len(y):
            c.append(x[-1])
            return c
        else:
            c.append(y[-1])
            return c
