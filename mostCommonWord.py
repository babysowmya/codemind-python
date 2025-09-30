class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
     a = re.findall(r'\w+',paragraph.lower())
     c = Counter(i for i in a if i not in banned)
     return c.most_common(1)[0][0]
