class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        c = [i for i in nums if i%2==0]
        if not c:
            return 0
        d = 0
        for i in range(len(c)):
            d = d|c[i]
        return d
