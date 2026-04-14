# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Traverse through linked list, adding nodes to seen table.

        # Each node we visit check if in seen, if so return True

        seen = set()

        while head:

            if head in seen:
                return True

            seen.add(head)
            head = head.next

        return False


        