class Solution:
    def leftRotate(self, arr, d):
        e = []
        for i in range(d,len(arr)):
            e.append(arr[i])
        for i in range(d):
            e.append(arr[i])
        arr[:]=e
        return arr
