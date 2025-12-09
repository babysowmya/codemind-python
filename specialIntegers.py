from typing import List
class Solution:
    def specialIntegers(self, n : int, arr : List[int]) -> int:
        a = set(arr)
        c = 0
        for i in a:
            if i-1 in a and i+1 in a:
                c = c+1
        return c
