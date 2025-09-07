class Solution:
	def removeCharacters(self, s):
		c = ""
		for i in s:
		    if ord(i)>=48 and ord(i)<=57:
		        c = c+i
		return c
