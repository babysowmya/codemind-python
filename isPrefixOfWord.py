class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        c = []
        for i in sentence:
            if i.startswith(searchWord):
                c.append(sentence.index(i)+1)
                break
        if c:
            return c[0]
        else:
            return -1
