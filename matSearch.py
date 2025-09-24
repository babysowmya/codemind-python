class Solution:
	def matSearch(self, mat, x):
		for i in mat:
		    if x in i:
		        return True
		return False
