class Solution:
    def sort_except_k(self, arr, k):
        a = arr[k]
        arr.pop(k)
        arr.sort()
        arr.insert(k,a)
        return arr
