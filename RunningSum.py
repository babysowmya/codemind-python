class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c = []
        sum = 0
        for i in range(len(nums)):
            sum = sum+nums[i]
            c.append(sum)
        return c
