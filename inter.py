class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if(len(nums)==1):
            return sorted(nums[0])
        else:
            c = set(nums[0])
            for i in range(1,len(nums)):
                c = c.intersection(set(nums[i]))
            return sorted(list(c))
