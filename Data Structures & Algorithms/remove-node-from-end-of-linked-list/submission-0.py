# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = None
        q = head
        len_list = 0
        curr = head
        while (curr != None):
            len_list += 1
            curr = curr.next
        #print(len_list)
        for i in range(len_list-n):
            p = q
            q = q.next
        #print(q.val)
        if (q == head):
            return q.next
        elif (q.next == None):
            p.next = None
        else:
            p.next = q.next
        return head

        