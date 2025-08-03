class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for i in c1:
            if i in c2:
                t = min(c1[i],c2[i])
                res.extend([i]*t)
        return res
