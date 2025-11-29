class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        a = sum(nums)
        if a%k==0:
            return 0
        else:
            return a%k
