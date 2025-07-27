class Solution:
    def thirdLargest(self,arr):
        a = max(arr)
        if len(arr)<3:
            return -1
        else:
            arr.remove(a)
            b = max(arr)
            arr.remove(b)
            return max(arr)
