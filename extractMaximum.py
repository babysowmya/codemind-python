class Solution:
    def extractMaximum(self,S): 
        c = ""
        d = []
        for i in range(len(S)):
            if S[i].isdigit():
                c = c+S[i]
                if i==len(S)-1 or not S[i+1].isdigit():
                    d.append(int(c))
                    c = ""
        if d:
            return max(d)
        return -1
