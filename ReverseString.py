class Solution:
     def reverseString(self, s: str) -> str:
         c = ""
         for i in s:
             c = i+c
         return c
