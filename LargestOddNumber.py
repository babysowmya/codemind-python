class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = list(num)
        while num and int(num[-1])%2==0:
            num.pop()
        if num:
            return ''.join(num)
        return ""
