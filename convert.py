class Solution:
    def convert(self, s):
        a = s.split()
        return ' '.join(i.capitalize() for i in a)
