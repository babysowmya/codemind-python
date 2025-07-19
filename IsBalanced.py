class Solution:
    def isBalanced(self, num: str) -> bool:
        res = list(num)
        c = 0
        d = 0
        for i in range(0,len(res)):
            if i%2==0:
                c = c+int(res[i])
            else:
                d = d+int(res[i])
        return c==d
