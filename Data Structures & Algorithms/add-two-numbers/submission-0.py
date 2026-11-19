# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def helper(self, node1: ListNode, node2: ListNode, carry=0):
        if (node1 == None and node2 == None):
            if (carry == 1):
                return ListNode(carry)
            return None
        else:
            digit = carry
            if (node1 != None):
                digit += node1.val
            if (node2 != None):
                digit += node2.val
            carry = digit//10
            head = ListNode(digit%10)
            if (node1 == None):
                head.next = self.helper(None, node2.next, carry)
            elif (node2 == None):
                head.next = self.helper(node1.next, None, carry)
            else:
                head.next = self.helper(node1.next, node2.next, carry)
            return head

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        return self.helper(l1, l2)
        
        