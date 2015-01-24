__author__ = 'bowiehsu'
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        #DSF
        if root == None:
            return 0
        #recursion
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        if left>=right:
            return left+1
        else:
            return right+1