class Solution:
    def minAnd2ndMin(self, arr):
        c = []
        arr = list(set(arr))
        arr.sort()
        if len(arr)<2:
            c.append(-1)
        else:
            one = arr[0]
            sec = arr[1]
            c.append(one)
            c.append(sec)
        return c
