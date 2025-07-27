class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        c = list(map(list,zip(*matrix)))
        return c
