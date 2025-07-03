class Solution:
    def firstOccurence(self,txt,pat):
        if pat not in txt:
            return -1
        else:
            return txt.index(pat)
