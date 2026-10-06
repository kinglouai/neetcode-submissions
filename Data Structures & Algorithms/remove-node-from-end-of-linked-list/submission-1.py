# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        l=1
        cur=head
        while cur.next is not None:
            cur=cur.next
            l+=1
        l-=n
        cur=head
        prv=None
        while l>0:
            prv=cur
            cur=cur.next
            l-=1
        print(cur.val)
        if prv is not None:
            prv.next=cur.next
        else:
            head=cur.next
        return head        
