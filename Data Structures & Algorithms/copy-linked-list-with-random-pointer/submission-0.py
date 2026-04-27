"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Iterate through old list and make new copy with new nodes and links to new nodes
        # Create a map that links old nodes to new nodes
        # Pass through the list again and add the random links to their corrosponding nodes

        curr = head
        new_curr = Node(0)
        new_head = new_curr
        old_to_new = {}

        while curr:
            new_curr.next = Node(curr.val)
            new_curr = new_curr.next # Make a copy of next node 

            old_to_new[curr] = new_curr

            curr = curr.next

        # Now we have to pass through again and link the randoms according to the old list 

        curr = head
        new_curr = new_head.next

        while curr:
            if curr.random:
                new_curr.random = old_to_new[curr.random]

            curr = curr.next
            new_curr = new_curr.next

        return new_head.next


