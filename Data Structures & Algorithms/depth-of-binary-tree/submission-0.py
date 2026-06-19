# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.dfs(root.left, 1), self.dfs(root.right, 1))
    
    def dfs(self, node, depth):
        if not node:
            return depth
        
        return max(self.dfs(node.left, depth+1), self.dfs(node.right, depth+1))


        