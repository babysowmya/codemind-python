class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = []
        d = []
        for i in arr2:
            if i in arr1:
                a = arr1.count(i)
                for j in range(a):
                    c.append(i)
        for i in arr1:
            if i not in c:
                d.append(i)
        d = sorted(d)
        return c+d
