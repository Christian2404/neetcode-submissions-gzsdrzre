# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        dq = deque()

        if root:
            dq.append(root)

        while dq:

            curr = dq.pop()

            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)

        return root