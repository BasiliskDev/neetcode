# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        largest = -300000000
        def maxPathHelper(node):
            nonlocal largest
            if (node == None):
                return 0
            maxPathLeft = maxPathHelper(node.left)
            maxPathRight = maxPathHelper(node.right)
            currPathLength = max(node.val + max(maxPathLeft, maxPathRight), node.val)
            largest = max(largest, currPathLength, node.val + maxPathLeft + maxPathRight)
            return currPathLength
        x = maxPathHelper(root)
        return largest
        