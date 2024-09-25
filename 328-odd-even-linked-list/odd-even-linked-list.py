# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next: return head

        even_head = head.next
        cur_odd = head
        cur_even = head.next

        while cur_odd.next and cur_even.next:
            cur_odd.next= cur_odd.next.next
            cur_even.next = cur_even.next.next
            cur_odd = cur_odd.next
            cur_even = cur_even.next
        cur_odd.next = even_head

        return head
        