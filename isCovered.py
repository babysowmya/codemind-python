class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        c = []
        for i in ranges:
            c = c+list(range(i[0],i[1]+1))
        for j in range(left,right+1):
            if j not in c:
                return False
        return True
