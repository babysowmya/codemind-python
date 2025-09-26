class Solution:
    def uniqueId(self, arr):
        c = []
        for i in arr:
            if i not in c:
                c.append(i)
        return c
