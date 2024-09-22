# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        myStore = []

        current = head

        while current:
            if id(current) in myStore:
                return True

            myStore.append(id(current))

            current = current.next
        
        return False
