class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        c = []
        d = []
        for i in range(len(arr)):
            if arr[i]<=x:
                c.append(arr[i])
            if arr[i]>=x:
                d.append(arr[i])
        if not c and not d:
            return -1,-1
        elif not c:
            return -1,min(d)
        elif not d:
            return max(c),-1
        else:
            return max(c),min(d)
