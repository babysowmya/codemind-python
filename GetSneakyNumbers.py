from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = []
        a = Counter(nums)
        for i in nums:
            if a[i]==2:
                c.append(i)
        res = list(set(c))
        res.sort()
        return res
