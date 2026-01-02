class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        a = sorted(nums)
        c = []
        for i in range(len(a)):
            for j in range(len(a)):
                if i<j and nums[i]<nums[j]:
                    c.append(nums[j]-nums[i])
        if c:
            return max(c)
        else:
            return -1
