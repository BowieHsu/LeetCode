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
        #print root.val
        if root == None:
            return None
        if root.left and root.right:
            root.left.next = root.right
            self.connect(root.left)
            self.connect(root.right)
            self.helper(root.left,root.right)
        return root
    def helper(self,root1,root2):
        if root1.next == root2 and root1.right and root2.left:
            root1.right.next = root2.left
            self.helper(root1.right,root2.left)
        if root1.right == None or root2.left == None:
            return None

instance = Solution()
root,root2,root3,root4,root5,\
root6,root7,root8,root9,root10,root11,root12,root13,root14,root15 = TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(5),TreeNode(6),TreeNode(7),\
    TreeNode(8),TreeNode(9),TreeNode(10),TreeNode(11),TreeNode(12),TreeNode(13),TreeNode(14),TreeNode(15)
root.left,root.right = root2,root3
root2.left,root2.right = root4,root5
root3.left,root3.right = root6,root7
root4.left,root4.right = root8,root9
root5.left,root5.right = root10,root11
root6.left,root6.right = root12,root13
root7.left,root7.right = root14,root15
ras = instance.connect(root)
print ras.left.right.right.next.val
