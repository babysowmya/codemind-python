class Solution:
    def reverseWords(self, s: str) -> str:
        c = ""
        for i in s.split():
            c = c+i[::-1]+" "
        return c.strip()
