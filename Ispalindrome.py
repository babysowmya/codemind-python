class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s[::-1]
        return s==a
