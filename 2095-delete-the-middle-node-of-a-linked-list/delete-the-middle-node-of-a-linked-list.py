# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # find n
        # current = head
        # n = 0

        # while current:
        #     current = current.next
        #     n += 1
        
        # middle = n//2

        # dummy = ListNode(0)
        # dummy.next = head

        # current = dummy

        # while middle != 0:
        #     current = current.next
        #     middle -= 1
        
        # current.next = current.next.next

        # return dummy.next

        if not head or not head.next:
            return None

        fast = head
        slow = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head