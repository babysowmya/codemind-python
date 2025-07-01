class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        c = []
        for i in range(len(nums)):
            x = pow(nums[i],2)
            c.append(x)
        c.sort()
        return c
