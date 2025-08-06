class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        total = sum(map(int,str(num)))
        return self.addDigits(total)
