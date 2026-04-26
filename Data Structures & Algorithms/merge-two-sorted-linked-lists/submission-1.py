# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # While elements in either list
        # Append smaller element to new list 

        res = ListNode
        start = res

        while list1 or list2:

            if list1 is None:
                res.next = list2
                return start.next

            if list2 is None:
                res.next = list1
                return start.next

            if list1.val <= list2.val:
                res.next = list1
                res = res.next
                list1 = list1.next
            else:
                res.next = list2
                res = res.next
                list2 = list2.next






