class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1),len(word2))
        d = []
        for i in range(n):
            d.append(word1[i])
            d.append(word2[i])
        if len(word1)>len(word2):
            d = ''.join(d)+word1[n:]
        if len(word2)>len(word1):
            d = ''.join(d)+word2[n:]
        return ''.join(d)
