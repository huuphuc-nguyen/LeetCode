# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        
        maxi = 0
        for i in range(len(arr)//2):
            sum = arr[i] + arr[len(arr)-1-i]
            maxi = max(maxi, sum)

        return maxi
