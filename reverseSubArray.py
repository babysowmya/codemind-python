class Solution:
	def reverseSubArray(self,arr,l,r):
	    a = arr[:l-1]
	    b = arr[l-1:r][::-1]
	    c = arr[r:]
	    return a+b+c
