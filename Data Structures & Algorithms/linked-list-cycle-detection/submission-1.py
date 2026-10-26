# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        index = -1
        # handle initial setup and base case of 0 or 1 length list 
        if head and head.next:
            curr = head
            _next = head.next
        else:
            return False

        seen = {}
        cur_idx = 0

        # iterate until the end of the list or a cycle
        while _next and index == -1:

            if _next in seen:
                index = seen[_next]
                return True
            
            # add seen node to seen dict (O(1) lookup)
            seen[_next] = cur_idx
            cur_idx += 1

            # update pointers
            temp = _next
            _next = _next.next
            curr = temp


        
        # will only exit loop if you have iterated through the entre list
        # and no loop was detected
        return False
        