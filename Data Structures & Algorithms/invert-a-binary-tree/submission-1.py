# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Base case: no children, return

        res = root

        if root is None:
            return

        # Recursive case: swap l and r, call on children 
        else:
            temp = root.left
            root.left = root.right
            root.right = temp

            self.invertTree(root.right)
            self.invertTree(root.left)

        return root

