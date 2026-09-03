class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        s = set()
        n = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    s.add(i)
                    n.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in s or j in n:
                    matrix[i][j]=0
