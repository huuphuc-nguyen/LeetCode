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
        # Find the length
        len = 1
        current = head

        while current.next is not None:
            current = current.next
            len += 1

        # find the index counted from the beginning
        # 5, n = 2, index to delete: 4: 5 - n + 1

        # current at index 3
        # current.next = cr.next.next
        
        prev_del_position = len - n

        if len == 1:
            return None
        
        if prev_del_position == 0:
            return head.next

        current = head
        for i in range(1, prev_del_position):
            current = current.next
        
        current.next = current.next.next

        return head