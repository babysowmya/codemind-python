class Solution:
	def onlyFirstAndLastAreSet(self, n):
	    a = list(str(bin(n)[2:]))
	    if a[0]=='1' and a[-1]=='1':
	        a.remove(a[0])
	        a.remove(a[-1])
	    if '1' in a:
	        return 0
	    else:
	        return 1
