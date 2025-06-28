class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        a = n*n
        if a*w<=maxWeight:
            return a
        else:
            for i in range(a,-1,-1):
                if i*w<=maxWeight:
                    return i
