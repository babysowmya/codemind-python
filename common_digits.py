class Solution:
	def common_digits(self, nums):
	    b = 0
	    c = []
	    for i in nums:
	        a = list(str(i))
	        for j in range(len(a)):
	            if int(a[j]) not in c:
	                c.append(int(a[j]))
	    return sorted(c)
