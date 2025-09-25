class Solution:
    def checkRecord(self, s: str) -> bool:
        a = Counter(s)
        if a["A"]<2 and "LLL" not in s:
            return True
        return False
