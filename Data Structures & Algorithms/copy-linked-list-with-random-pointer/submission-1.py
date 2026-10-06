"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is not None:    
            l=Node(head.val)
        else:
            return Node(0).next
        start=l
        cur=head 
        d=dict()
        while cur.next is not None:
            l.val=cur.val 
            l.next = Node(cur.next.val)
            d[cur]=l
            l=l.next
            cur=cur.next
        d[cur]=l
        cur=head
        l=start
        while cur is not None:
            if cur.random is not None:
                l.random=d[cur.random]
            else:
                l.random=None
            l=l.next
            cur=cur.next
        
        return start


        