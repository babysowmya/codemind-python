class Solution:
    def smallestNumber(self, n: int) -> int:
        i=n
        while i>=n:
            a = bin(i)[2:]
            if '0' not in a:
                return i
            i=i+1
