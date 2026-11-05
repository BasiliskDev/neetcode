# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        head = self.helper(head, head.next)
    
    def helper(self, node1, node2):
        if (node2 == None):
            return node1
        left = self.helper(node1, node2.next)
        if (left == None):
            return None
        if (left.next == node2 or left == node2):
            node2.next = None
            return None
        tmp = left.next
        left.next = node2
        node2.next = tmp
        return tmp

