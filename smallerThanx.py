class Solution:
    def smallerThanX(self,arr,n,x):
        c = 0
        for i in arr:
           if i<x:
               c = c+1
        return c
