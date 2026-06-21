# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestors_p = None
        ancestors_q = None
        def traverse(node, ancestors, depth):
            nonlocal p,q,ancestors_p,ancestors_q
            if (node == None):
                return
            ancestors.append((node, depth))
            if (node.val == p.val):
                ancestors_p = ancestors.copy()
            if (node.val == q.val):
                ancestors_q = ancestors.copy()
            traverse(node.left, ancestors, depth+1)
            traverse(node.right, ancestors, depth+1)
            ancestors.pop()
        traverse(root, [], 0)
        ancestor = max(set(ancestors_p) & set(ancestors_q), key=lambda x: x[1])
        return ancestor[0]

        