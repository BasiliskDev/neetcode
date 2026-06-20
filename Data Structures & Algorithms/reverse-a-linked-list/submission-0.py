# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        def travel(node, prev):
            nonlocal res
            if (node == None):
                res = prev
                return
            travel(node.next, node)
            node.next = prev
        travel(head, None)
        return res

        