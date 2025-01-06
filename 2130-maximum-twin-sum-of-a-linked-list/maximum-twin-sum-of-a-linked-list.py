# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #arr = []
        # current = head
        # while current:
        #     arr.append(current.val)
        #     current = current.next
        
        # maxi = 0
        # for i in range(len(arr)//2):
        #     sum = arr[i] + arr[len(arr)-1-i]
        #     maxi = max(maxi, sum)

        # return maxi

        # find the middle node
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the 2nd half
        sec_head = slow
        prev = None
        current = sec_head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # reverse through 2 list
        c1 = head
        c2 = prev
        maxi = 0
        while c1 and c2:
            maxi = max(maxi, c1.val + c2.val)
            c1=c1.next
            c2=c2.next
        
        return maxi

