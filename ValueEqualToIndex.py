class Solution:
    def valueEqualToIndex(self, arr):
        c = []
        for i in range(len(arr)):
            if i+1==arr[i]:
                c.append(arr[i])
        return c
