class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c = []
        for i in range(len(nums)):
            if nums[i]==1:
                c.append(i)
        for i in range(len(c)-1):
            a = abs(c[i]-c[i+1])
            if a-1<k:
                return False
        return True
