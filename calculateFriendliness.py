class Solution:
    def calculateFriendliness(self, arr):
        c = 0
        for i in range(1,len(arr)):
            c = c+abs(arr[i]-arr[i-1])
        c = c+abs(arr[0]-arr[-1])
        return c
