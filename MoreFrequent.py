class Solution:
    def moreFrequent(self, arr, x, y):
        if x and y in arr:
            a = arr.count(x)
            b = arr.count(y)
            if a>b:
               return x
            elif a<b:
               return y
            else:
               return min(x,y)
        elif x in arr and y not in arr:
            return x
        elif y in arr and x not in arr:
            return y
        else:
            return min(x,y)
