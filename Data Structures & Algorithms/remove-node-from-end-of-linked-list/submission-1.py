# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        sz = 0
        curr, start = head, head

        # Check the size of the list 
        while head:
            sz += 1
            head = head.next

        # Iterate to n's position
        position_to_remove = sz - n # Zero indexed position

        prev = None
        print(f"position to remove: {position_to_remove}")
        for _ in range(position_to_remove):
            prev = curr
            curr = curr.next

        # remove elem & return start

        if prev is None: # Removing only elem
            start = curr.next 
        else: # Remove and create link
            prev.next = curr.next

        return start


        
