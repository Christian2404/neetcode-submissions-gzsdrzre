# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse_linked_list(head: ListNode) -> ListNode:

            prev = None
            curr = head

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp 

            return prev
        
        # Use a fast and slow pointer to get to midpoint of list

        slow = head
        fast = head

        while fast and fast.next:

            prev = slow 
            slow = slow.next
            fast = fast.next.next
        
        # Create new list from mid -> end
        l2 = slow.next
        slow.next = None

        # Reverse new list
        l2 = reverse_linked_list(l2)

        # Merge two lists
        curr = head

        while l2 and curr:

            temp1 = curr.next
            temp2 = l2.next

            curr.next = l2
            l2.next = temp1

            curr = temp1
            l2 = temp2

        