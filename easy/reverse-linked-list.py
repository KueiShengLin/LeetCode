# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return 

        # stack
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        now = stack.pop()
        res_head = now
        
        while stack:
            now.next = stack.pop()
            now = now.next
            
        now.next = None
        return res_head
                
            
            