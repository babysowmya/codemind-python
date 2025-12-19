class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        c = []
        for i in range(len(nums)):
            a = nums[:i]
            b = nums[i+1:]
            c.append(abs(sum(a)-sum(b)))
        return c
