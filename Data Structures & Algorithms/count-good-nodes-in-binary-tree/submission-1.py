# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(currMaxVal, currNode):
            if (currNode == None):
                return 0
            if (currNode.val >= currMaxVal):
                return dfs(currNode.val, currNode.left) + dfs(currNode.val, currNode.right) + 1
            return dfs(currMaxVal, currNode.left) + dfs(currMaxVal, currNode.right)
        return dfs(root.val, root)
            
        