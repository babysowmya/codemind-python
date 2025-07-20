class Solution:
    def convertFive(self, n):
        c = str(n)
        c = c.replace('0','5')
        return int(c)
