import math
class Solution:
    def findMajority(self, arr):
        a = math.floor(len(arr)/3)
        c = []
        d = []
        for i in arr:
            if i not in c:
                c.append(i)
        for i in c:
            if arr.count(i)>a:
                d.append(i)
        return sorted(d)
