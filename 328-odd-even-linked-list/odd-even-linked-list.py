# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1 2 3 4 5
        #       e o
        
        # current odd
        # current even
        # odd head list : 1
        # even head list: 2
        # return odd -> even

        if not head or not head.next:
            return head

        evenhead = head.next

        current = head
        n = 1
        prev = None
        while current.next:
            temp = current.next
            current.next = current.next.next
            prev = current
            current = temp
            n += 1

        print(evenhead)
        print(n)
        print(current)

        if n % 2 == 1:
            current.next = evenhead
        else:
            prev.next = evenhead

        return head


        


        