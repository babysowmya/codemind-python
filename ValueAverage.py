class Solution:
    def averageValue(self, nums: List[int]) -> int:
        c = 0
        d = 0
        for i in nums:
            if i%3==0 and i%2==0:
                c =c+i
                d = d+1
        if d==0:
            return 0
        else:
            return c//d
