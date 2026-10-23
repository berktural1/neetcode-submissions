# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # you could do this recursively but that won't work for lists resulting in over
        # 1000 recursive calls in Python nad it requires O(n+m) extra space

        # sorting the linked lists with pointers is O(1) extra space and what I am going
        # to work on

        dummy = ListNode() # know you need a dummy to handle empty cases
        merged = dummy # create another pointer that keeps track of moving through
                       # where dummy will serve to reference beginning of list

        while list1 and list2: # while both lists are not empty

            if list1.val < list2.val:
                merged.next = list1 # add list1 node to the list
                merged = merged.next
                list1 = list1.next  # update pointer for list1
            else: # handles case of equality and list2 val < list1 val
                merged.next = list2
                merged = merged.next
                list2 = list2.next

        # handle edge cases and situations where one list is still non-empty
        # pointing to it tacks it on the linked list
        if list1:
            merged.next = list1
        if list2:
            merged.next = list2
        
        return dummy.next # use original pointer to refer to first sorted node from 2 lists

        # O(n+m) time
        # O(1) space
        