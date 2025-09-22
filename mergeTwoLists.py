class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []
        while list1:
            arr1.append(list1.val)
            list1 = list1.next
        while list2:
            arr2.append(list2.val)
            list2 = list2.next
        co = sorted(arr1+arr2)
        d = ListNode(0)
        c = d
        for i in co:
            c.next = ListNode(i)
            c = c.next
        return d.next
