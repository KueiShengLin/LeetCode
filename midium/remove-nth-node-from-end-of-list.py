# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # list length
        list_len = 1
        now_node = head
        while now_node.next != None:
            list_len += 1
            now_node = now_node.next
        # remove nth node
        now_node = head
        remove_n = list_len - n + 1
        if remove_n == 1:
            head = head.next
            return head
        
        for i in range(1, remove_n):
            if i == remove_n - 1:
                now_node.next = now_node.next.next
            else:
                now_node = now_node.next
        
        return head