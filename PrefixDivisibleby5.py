class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        c = ""
        d = []
        for i in nums:
            c = c+str(i)
            a = int(c,2)
            if a%5==0:
                d.append(True)
            else:
                d.append(False)
        return d
