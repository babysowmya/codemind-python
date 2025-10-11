class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a = s1.split()+s2.split()
        c = []
        b = Counter(a)
        for i in b:
            if b[i]==1:
                c.append(i)
        return c
