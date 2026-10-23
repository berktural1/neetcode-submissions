# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # iterate though going forward, switching pointers?
        
        if head:
            curr = head
            _next = curr.next
            # for first node, set its next = None as it will be the end of the list
            curr.next = None
        else:
            return head

        while _next: # while there is
            #curr.next = prev
            tmp = _next.next # point to the next object to keep track of it
            _next.next = curr # reverse, point to current
            curr = _next # update current pointer
            _next = tmp # update next pointer

        return curr


