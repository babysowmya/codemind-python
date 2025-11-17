class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = []
        d = []
        for i in nums:
            if i%2==0:
                c.append(i)
        if not c:
            return -1
        a = Counter(c)
        m = max(a.values())
        for i in c:
            if a[i]==m:
                d.append(i)
        return min(d)
