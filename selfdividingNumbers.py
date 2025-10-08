class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        d = []
        for i in range(left,right+1):
            a = str(i)
            a.split()
            c = 0
            for j in a:
                if j=='0' or i%int(j)!=0:
                    break
                c=c+1
            if c==len(a):
                d.append(i)
        return d
