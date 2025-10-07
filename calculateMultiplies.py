class Solution:
    def calculateMultiples(self, n):
        i=1
        c = []
        while i<=10:
            c.append(i*n)
            i=i+1
        c = c[::-1]
        print(*(c))
