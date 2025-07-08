class Solution:
	def countOddEven(self, arr):
	    c = 0
	    d = 0
	    for i in arr:
	        if i%2!=0:
	            c = c+1
	        else:
	            d = d+1
	    return c,d
