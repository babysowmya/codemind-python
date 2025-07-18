from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:   
        z = Counter(s)
        return len(set(z.values()))==1
