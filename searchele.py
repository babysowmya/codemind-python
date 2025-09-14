class Solution:
    def searchEle(self,arr, x):
        if x in arr:
            return True
        else:
            return False
    def insertEle(self,arr, y, yi):
        arr.insert(yi,y)
        if arr:
            return True
        else:
            return False
    def deleteEle(self,arr, z):
        if z in arr:
            arr.remove(z)
            return True
