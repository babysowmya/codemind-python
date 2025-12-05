class Solution:
    def countryAtWar(self, arr1, arr2):
        c = 0
        d = 0
        for i in range(len(arr1)):
            if arr1[i]>arr2[i]:
                c = c+1
            else:
                d = d+1
        if c>d:
            return "A"
        elif c<d:
            return "B"
        else:
            return "DRAW"
