# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depths = {}
        def assign_depth(root, depth):
            if not root:
                return
            depths[root] = depth
            assign_depth(root.left, depth+1)
            assign_depth(root.right, depth+1)
        assign_depth(root, 0)

        dq = deque([root])
        ret = []
        currdepth = 0
        currlayer = []
        while dq:
            node = dq.popleft()
            if not node:
                continue
            if depths[node] != currdepth:
                currdepth = depths[node]
                ret.append(currlayer)
                currlayer=[]
            currlayer.append(node.val)
            dq.append(node.left)
            dq.append(node.right)
        if (currlayer != []):
            ret.append(currlayer)
        return ret



        