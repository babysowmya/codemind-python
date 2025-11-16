from collections import Counter
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        a = Counter(nums)
        c = 0
        for i in nums:
            if a[i]%k==0:
                c = c+i
        return c
