# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)
            
            if abs(l - r) > 1:                
                return float('-inf')

            return max(l, r) + 1 # return height max height of subtree, l and r

        if dfs(root) < 0:
            return False     
        return True