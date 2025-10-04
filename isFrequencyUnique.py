from collections import Counter
from typing import List
class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        a = Counter(arr)
        b = list(a.values())
        c = set(b)
        return len(b)==len(c)
