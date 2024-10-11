# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        l_list_head = ListNode(0)
        ge_list_head = ListNode(0)

        current_less = l_list_head
        current_ge = ge_list_head

        while head:
            if head.val < x:
                current_less.next = head
                current_less = current_less.next
            else:
                current_ge.next = head
                current_ge = current_ge.next
            head = head.next
        
        current_less.next = ge_list_head.next
        current_ge.next = None

        return l_list_head.next