# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        length = 1
        current = head

        while current.next is not None:
            length += 1
            current = current.next

        delete_pos = length - n + 1

        if delete_pos == 1:
            return head.next
        
        current = head
        for i in range (1, delete_pos - 1):
            current = current.next

        current.next = current.next.next

        return head