from collections import Counter
class Solution:
    def secFrequent(self, arr, n):
        a = Counter(arr)
        b = list(a.values())
        c = max(b)
        b.remove(c)
        d = max(b)
        for i in a:
            if a[i]==d:
                return i
                break
        return -1
