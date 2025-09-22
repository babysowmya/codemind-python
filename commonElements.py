class Solution:
    def commonElements(self, arr1, arr2, arr3):
        a = set(arr1)
        b = set(arr2)
        c = set(arr3)
        d = a.intersection(b)
        e = b.intersection(c)
        f = d.intersection(e)
        z = sorted(list(f))
        return z
