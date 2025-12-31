class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        b = a[::-1]
        c = 0
        d = 0
        for i in range(k):
            c = c+a[i]
            d = d+b[i]
        return abs(c-d)
