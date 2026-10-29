# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        # naive approach: keep track of seen in a list or dict (better)
        # and check if you have seen the "next" node before
        # this is O(n) time O(n) extra space

        # there is an algorithm that does this better by using 2
        # pointers and advancing one by 2 steps each time and the 
        # other by 1.
        # this is O(n) time but O(1) extra space

        # will ignore hte idx part for now b/c I am not sure
        # how it is relevant

        # if list is 0 length, it has to be false
        if not head:
            return False

        pt_1 = head
        pt_2 = head.next

        # this works by checking if they are point to the same object
        # as you iterate through length of list

        # edge case: 0 length list

        while pt_1 and pt_2 and pt_2.next: # catches case where 
                                               # list ends and can't 
                                               # advance 2 pos
            if pt_1 == pt_2:
                return True

            pt_1 = pt_1.next
            pt_2 = pt_2.next.next

        return False

    # issue ran into: second pointer can't advance by 2
        