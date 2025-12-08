class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)-1):
            a = sum(nums[:i+1])
            b = sum(nums[i+1:])
            if abs(a-b)%2==0:
                c = c+1
        return c
