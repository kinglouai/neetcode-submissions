# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f=head
        s=head
        while f is not None and f.next is not None:
                f=f.next.next
                s=s.next
        prv=None
        cur=s.next
        s.next=None
        print("hello")
        while cur is not None:
            nex=cur.next
            cur.next=prv
            prv=cur
            cur=nex
        f=head
        s=prv 
        while s is not None:
            nex1=f.next
            nex2=s.next
            f.next=s
            s.next=nex1
            f=nex1
            s=nex2
