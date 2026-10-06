class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        l = ListNode()
        cur3 = l
        
        while (cur1 is not None) and (cur2 is not None):
            s = cur1.val + cur2.val
            if s > 9:
                cur3.val = s - 10
                
                if cur1.next is not None:
                    cur1.next.val += 1
                elif cur2.next is not None:
                    cur2.next.val += 1
                else:
                    cur1.next = ListNode(1)
            else:
                cur3.val = s
                
            cur1 = cur1.next
            cur2 = cur2.next            
            if (cur1 is not None) and (cur2 is not None):
                cur3.next = ListNode()
                cur3 = cur3.next
                
        if cur1 is not None:
            cur3.next = cur1
        elif cur2 is not None:
            cur3.next = cur2
            
        temp = cur3.next
        while temp is not None:
            if temp.val > 9:
                temp.val -= 10
                if temp.next is not None:
                    temp.next.val += 1
                else:
                    temp.next = ListNode(1)
            temp = temp.next
            
        return l