class Solution:
    def count_elements(self, arr):
        a = float('-inf')
        c = 0
        for i in range(len(arr)):
            if arr[i]>a:
                c = c+1
                a = arr[i]
        return c
