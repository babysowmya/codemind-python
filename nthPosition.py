class Solution:
    def nthPosition (self, n):
        pos = 1
        while pos * 2 <= n:
            pos *= 2
        return pos
