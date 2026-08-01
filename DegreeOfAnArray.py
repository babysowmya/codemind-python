from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        a = Counter(nums)
        v = a.values()
        m = max(v)
        c = []
        for i in a:
            if a[i]==m:
                c.append(i)
        res = float('inf')
        for i in c:
            x = []
            for j,k in enumerate(nums):
                if k==i:
                    x.append(j)
            l = x[-1]-x[0]+1
            res = min(res,l)
        return res
