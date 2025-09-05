class Solution:
    def searchMatrix(self,matrix, x): 
    	for i in matrix:
    	    for j in i:
    	        if j==x:
    	            return True
    	return False
