from itertools import permutations
class Solution:
    def binarySubstring(self, s):
        a = s.count('1')
        return a*(a-1)//2
