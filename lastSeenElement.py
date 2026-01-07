class Solution:
    def lastSeenElement(self, arr):
        s = set()
        c = []
        for i in range(len(arr)-1,-1,-1):
            if arr[i] not in s:
                s.add(arr[i])
                c.append(arr[i])
        return c[-1]
