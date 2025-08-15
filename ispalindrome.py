class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        c = ""
        for i in s:
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
                c = c+i
        a = c[::-1]
        return  c==a
