class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        c = 1
        a = len(arr)
        for i in range(0,a-1):
            if arr[i]<=arr[i+1]:
                c = c+1
        if c==a:
            return True
        else:
            return False
