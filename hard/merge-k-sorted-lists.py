# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = list(filter(None, lists))
        if lists == [] :
            return None
        
        h = []
        for nid, node in enumerate(lists):
            if node != None:
                heappush(h, (node.val, nid)) 
        
        min_info = heappop(h)
        now = lists[min_info[1]]
        res = now
        
        if now.next != None:
            lists[min_info[1]] = lists[min_info[1]].next
            heappush(h, (lists[min_info[1]].val, min_info[1]))
            
        while h:
            min_info = heappop(h)
            now.next = lists[min_info[1]]
            now = now.next
            if now.next != None:
                lists[min_info[1]] = lists[min_info[1]].next
                heappush(h, (lists[min_info[1]].val, min_info[1]))

        return res