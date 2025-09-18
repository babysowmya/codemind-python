from collections import Counter
class Solution:
	def countSubstring(self, s):
		a = Counter(s)
		c = 0
		for i in a:
		    n = a[i]
		    c = c+n+(n*(n-1))//2
		return c
