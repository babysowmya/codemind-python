class Solution:
    def countNumberswith4(self, n : int) -> int:
        c=0
        for i in range(1,n+1):
            a = str(i)
            if '4' in a:
                c = c+1
        return c
