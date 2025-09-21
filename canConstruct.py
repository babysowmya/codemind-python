from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = 0
        a = Counter(ransomNote)
        b = Counter(magazine)
        for i in a:
            if a[i]<=b[i]:
                c = c+a[i]
        return len(ransomNote)==c
