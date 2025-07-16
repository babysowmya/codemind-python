class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = []
        for i in nums1:
            if i in nums2:
                c.append(i)
        c = list(set(c))
        return c
