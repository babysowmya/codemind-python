class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        c = 1
        for i in range(1,max(nums)+2):
            if i not in nums:
                c = i
                break
        return c
