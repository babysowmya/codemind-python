class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c = 0
        d = 0
        for i in nums:
            if i>0:
                c = c+1
            if i<0:
                d = d+1
        return max(c,d)
