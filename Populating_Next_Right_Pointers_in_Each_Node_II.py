#encoding:utf-8
__author__ = 'bowiehsu'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        clone = root
        while clone:
            head = TreeNode(0)
            tail = head
            while clone:
                if clone.left:
                    tail.next = clone.left
                    tail = tail.next
                if clone.right:
                    tail.next = clone.right
                    tail = tail.next
                clone = clone.next
            clone = head.next
        return root

instance = Solution()
instance = Solution()
root,root2,root3,root4,root5,\
root6,root7,root8,root9,root10,root11,root12,root13,root14,root15 = TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(5),TreeNode(6),TreeNode(7),\
    TreeNode(8),TreeNode(9),TreeNode(10),TreeNode(11),TreeNode(12),TreeNode(13),TreeNode(14),TreeNode(15)

root.left,root.right = root2,root3
root2.left = root4
root4.left = root5
root3.right = root7
root7.left = root6

ras = instance.connect(root)
print ras.left.next.val
