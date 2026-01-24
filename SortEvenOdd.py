class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        c = []
        d = []
        e = []
        for i in range(len(nums)):
            if i%2!=0:
                c.append(nums[i])
            else:
                d.append(nums[i])
        c = sorted(c)[::-1]
        d = sorted(d)
        for i in range(len(nums)//2):
            e.append(d[i])
            e.append(c[i])
        if len(c)>len(d):
            e.append(c[-1])
        if len(d)>len(c):
            e.append(d[-1])
        return e
