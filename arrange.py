class Solution:
    def rearrange(self, arr):
        a = sorted(arr)
        n = len(a)
        l = a[:n//2]
        r = a[n//2:][::-1]
        c = []
        for i in range(n//2):
            c.append(r[i])
            c.append(l[i])
        if n%2==0:
            arr[:] = c
        else:
            if len(l)>len(r):
                c.append(l[-1])
            else:
                c.append(r[-1])
            arr[:] = c
