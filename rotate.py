class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        a = list(zip(*matrix))
        b = []
        for i in a:
            b.append(list(i)[::-1])
        matrix[:]=b
        return b
