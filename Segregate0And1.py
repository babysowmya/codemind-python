class Solution:
    def segregate0and1(self, arr):
        if 1 not in arr:
            return arr
        elif 0 not in arr:
            return arr
        else:
            arr.sort()
        return arr
