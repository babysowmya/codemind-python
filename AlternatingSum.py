class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        a = sum(nums[0::2])
        b = sum(nums[1::2])
        return a-b
