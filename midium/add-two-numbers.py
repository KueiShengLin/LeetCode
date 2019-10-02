class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_now = l1
        l2_now = l2
        l3 = ListNode(0)
        l3_now = l3
        v1, v2, now = 0,0,1
        while l1_now != None:
            v1 += l1_now.val * now
            l1_now = l1_now.next
            now *= 10
        
        now = 1
        while l2_now != None:
            v2 += l2_now.val * now
            l2_now = l2_now.next
            now *= 10
            
        v3 = v1 + v2
        
        while v3 >= 1:
            print(v3)
            temp = int(v3 % 10)
            l3_now.val = temp
            v3 = v3 // 10
            if v3 >= 1:
                l3_now.next = ListNode(0)
                l3_now = l3_now.next
            
        return l3