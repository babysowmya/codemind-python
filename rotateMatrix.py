class Solution:
    def rotateMatrix(self, mat):
        c = []
        for i in zip(*mat):
            c.append(i)
        mat[:] = c[::-1]
        return mat
