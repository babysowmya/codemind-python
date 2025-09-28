class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        a = bin(n)[2:][::-1]
        b = str(a)
        c = 0
        d = 0
        for i in range(len(b)):
            if b[i]=='1':
                if i%2==0:
                    c = c+1
                else:
                    d = d+1
        return [c,d]
