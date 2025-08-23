class Solution:
    def remainderWith7(self, str):
        a = 0
        for i in str:
            a = (a*10+int(i))%7
        return a
