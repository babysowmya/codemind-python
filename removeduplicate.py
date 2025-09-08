class Solution:
    def removeDuplicate(self, arr):
        s = set()
        c=[]
        for i in arr:
            if i not in s:
                s.add(i)
                c.append(i)
        return c
