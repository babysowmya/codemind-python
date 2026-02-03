class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c = []
        for i in sentences:
            a = i.split()
            c.append(len(a))
        return max(c)
