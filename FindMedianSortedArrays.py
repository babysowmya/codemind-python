class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1+nums2
        c.sort()
        if len(c)%2!=0:
            res = c[len(c)//2]
        else:
            x = c[len(c)//2]
            y = c[len(c)//2-1]
            res = (x+y)/2
        return res
