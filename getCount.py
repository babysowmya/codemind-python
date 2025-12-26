class Solution:
    def getCount(self, arr, num1, num2):
        a = 0
        b = 0
        for i in range(len(arr)):
            if arr[i]==num1:
                a = i
                break
        for j in range(len(arr)-1,-1,-1):
            if arr[j]==num2:
                b = j
                break
        if b-a>0:
            return b-a-1
        else:
            return 0
