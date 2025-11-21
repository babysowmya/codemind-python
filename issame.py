class Solution:
	def isSame(self, s):
	    c = ""
	    d = ""
	    for i in s:
	        if i.isalpha():
	            c = c+i
	        else:
	            d = d+i
	    if d=="":
	        return 0
	    if len(c)==int(d):
	        return 1
	    else:
	        return 0
