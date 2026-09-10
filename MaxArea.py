class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        z = 0
        while l<r:
            w = r-l
            m = min(height[l],height[r])
            res = w*m
            z = max(z,res)
            if height[l]<height[r]:
                l = l+1
            else:
                r = r-1
        return z
