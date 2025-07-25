from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = Counter(arr)
        b = list(a.values())  
        c = set(b)
        if len(b)==len(c):
            return True
        else:
            return False
