class Solution:
    def insertAtEnd(self, arr, val):
        arr.insert(len(arr)+1,val)
        return arr
