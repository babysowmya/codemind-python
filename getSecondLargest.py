class Solution:
    def getSecondLargest(self, arr):
        a = list(set(arr))
        b = sorted(a,reverse=True)
        if len(b)<2:
            return -1
        return b[1]
