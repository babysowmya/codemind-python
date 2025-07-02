class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
     c = []
     for i in range(len(nums)):
        if nums[i]%2==0:
            c.append(nums[i])
     for i in range(len(nums)):
        if nums[i]%2!=0:
            c.append(nums[i])
     return c
