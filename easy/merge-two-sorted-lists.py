# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:  
        # init res link list
        res = head = ListNode(-1)
        
        while l1 and l2:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
                res = res.next
            
            else:
                res.next = l2
                l2 = l2.next
                res = res.next
        
        # link remain numbers
        if l1 != None:
            res.next = l1
        elif l2 != None:
            res.next = l2
            
        return head.next
        
        
            