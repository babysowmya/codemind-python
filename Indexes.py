class Solution:
    def indexes(self, v, x):
        if x not in v:
            return [-1,-1]
        else:
            for i in range(0,len(v)):
                if v[i]==x:
                    a =  i
                    break
            for i in range(len(v)-1,-1,-1):
                if v[i]==x:
                    b = i
                    break
            return [a,b]
