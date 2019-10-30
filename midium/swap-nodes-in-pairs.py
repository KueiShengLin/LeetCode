# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        swap = False
        now_node = head
        last_node = head
        res_head = head
        last_pair_end = head
        
        if head == None or head.next == None:
            return head
        else:
            res_head = head.next
            
        while now_node != None:
            if swap is True:
                temp_node = now_node.next
                last_node.next = now_node.next
                now_node.next = last_node
                now_node = temp_node
                last_pair_end = last_node
            else:
                last_node = now_node
                if now_node.next != None:
                    last_pair_end.next = now_node.next
                    
                now_node = now_node.next
            swap = not swap
        return res_head