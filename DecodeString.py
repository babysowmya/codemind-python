class Solution:
    def decodeString(self, s: str) -> str:
        n=0
        cur=""
        stack = []
        for i in s:
            if i.isdigit():
                n = n*10+int(i)
            elif i=='[':
                stack.append((cur,n))
                n=0
                cur=""
            elif i==']':
                prev,rep = stack.pop()
                cur = prev+cur*rep
            else:
                cur+=i
        return cur
