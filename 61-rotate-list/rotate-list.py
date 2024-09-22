# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head

        list_len = 1

        counter = head

        while counter.next:
            list_len += 1
            counter = counter.next

        counter.next = head
        k = k % list_len
        
        new_end = head

        for i in range(list_len - k - 1):
            new_end = new_end.next

        new_start = new_end.next
        new_end.next = None

        return new_start