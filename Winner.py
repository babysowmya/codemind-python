from collections import Counter
class Solution:
    def winner(self,arr,n):
        a = Counter(arr)
        b = max(a.values())
        d = []
        e=[]
        for i in a:
            if a[i]==b:
                d.append(a[i])
                e.append(i)
        x = sorted(d)
        y = sorted(e)
        return y[0],x[0]
