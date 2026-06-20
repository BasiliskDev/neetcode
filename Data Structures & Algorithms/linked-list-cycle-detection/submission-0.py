# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        res = None
        def traverse(node):
            nonlocal res
            if (node == None):
                res = False
                return
            if (node in visited):
                res = True
                return
            visited.append(node)
            traverse(node.next)
        traverse(head)
        return res
            
        