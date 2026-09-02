class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        d = []
        for i in zip(*matrix):
            d.append(i[::-1])
        matrix[:]=d
        
