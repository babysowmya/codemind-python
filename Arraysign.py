class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c = 1
        for i in nums:
            if i==0:
               return 0
            elif i<0:
                c = c*-1
        return c
