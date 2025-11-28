class Solution:
    def check_duck(self, N):
        if N[0] == '0':
            return False
        for i in range(1, len(N)):
            if N[i] == '0':
                return True
        return False
