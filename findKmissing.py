class Solution:
    def findKthMissing(self, arr1, arr2, k):
        c = []
        a = set(arr2)
        for i in arr1:
            if i not in a:
                c.append(i)
        if len(c)<k:
            return -1
        return c[k-1]
