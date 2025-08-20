class Solution:
    def ReverseSort(self, s): 
        a = sorted(s,reverse = True)
        return ''.join(a)
