class Solution:
    def findFloor(self, arr, x):
        c = []
        for i in arr:
            if i<=x:
                c.append(i)
            else:
                break
        if c:
            return len(c)-1
        return -1
