class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        c =""
        d = ""
        for i in word1:
            c = c+i
        for i in word2:
            d = d+i
        return c==d
