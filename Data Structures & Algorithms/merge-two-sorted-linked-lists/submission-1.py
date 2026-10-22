# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # dummy node to handle fact we start with an empty output linked list
        dummy = ListNode()
        merged = dummy # point to that node / linked list of nodes


        while list1 and list2:

            # check values
            if list1.val < list2.val:
                merged.next = list1
                list1 = list1.next # update pointer
            else: # handles both hte case of equality and list2.val < list1.val
                merged.next = list2
                list2 = list2.next #update pointer
            
            # advance pointer in all situations:
            merged = merged.next
        
        # handle edge cases where only one list is empty
        if list1:
            merged.next = list1 #add rest of the linked list to output
        if list2:
            merged.next = list2 # same with list2
        
        return dummy.next

        