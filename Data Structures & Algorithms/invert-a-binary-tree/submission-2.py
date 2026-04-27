# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        dq = deque()

        if root is not None:
            dq.append(root)

        while dq:
            parent = dq.popleft()
            parent.left, parent.right = parent.right, parent.left

            if parent.left is not None:
                dq.append(parent.left)
            
            if parent.right is not None:
                dq.append(parent.right)

        return root 