from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        x = Counter(a)
        y = Counter(b)
        if x==y:
            return True
        else:
            return False
