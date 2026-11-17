# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        prevlevel = -1
        ret = []
        dq = deque([(root, 0)])
        while (len(dq)):
            currelement = dq.popleft()
            currnode = currelement[0]
            if (currnode == None):
                continue
            currlevel = currelement[1]
            if (prevlevel != currlevel):
                ret.append(currnode.val)
            prevlevel = currlevel
            dq.append((currnode.right, currlevel+1))
            dq.append((currnode.left, currlevel+1))
        return ret

        