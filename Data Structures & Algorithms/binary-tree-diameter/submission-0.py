# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        farthest1, max_diam1 = self.dfs(root.left)
        farthest2, max_diam2 = self.dfs(root.right)
        return max(max_diam1, max(max_diam2, farthest1+farthest2))
    
    def dfs(self, node):
        if not node:
            return 0, 0
        farthest1, max_diam1 = self.dfs(node.left)
        farthest2, max_diam2 = self.dfs(node.right)
        
        return max(farthest1, farthest2)+1, max(max_diam1, max(max_diam2, farthest1+farthest2))
        