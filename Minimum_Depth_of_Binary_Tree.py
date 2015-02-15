# encoding:utf-8
__author__ = 'bowiehsu'
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self,root):
        if root == None:
            return 0
        lmin = self.minDepth(root.left)
        rmin = self.minDepth(root.right)
        if lmin == 0 and rmin == 0:
            return 1
        #没有左子树的情况
        if lmin == 0:
            lmin = 65536
        #没有右子树的情况
        if rmin == 0:
            rmin = 65536
        return min(lmin,rmin)+1


Node1,Node2 = TreeNode(1),TreeNode(2)
Node1.left = Node2
Node = TreeNode(0)
instance = Solution()
print instance.minDepth(Node1)
