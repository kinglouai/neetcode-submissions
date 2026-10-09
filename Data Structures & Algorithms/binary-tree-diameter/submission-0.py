# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m=0
        def high(root):
            nonlocal m
            if not root:
                return -1
            else:
                l=high(root.left)
                r=high(root.right)
                d=l+r+2
                m=max(d,m)
                return 1+ max(l,r)
        high(root)
        return m
            