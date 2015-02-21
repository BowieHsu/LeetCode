__author__ = 'bowiehsu'

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self,root,sum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum
        print sum
        return  self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)



instance = Solution()
Node1,Node2,Node3,Node4,Node5,Node6,Node7 = TreeNode(5),TreeNode(4),TreeNode(8),TreeNode(11),TreeNode(13),TreeNode(4),TreeNode(2)
Node1.left,Node1.right = Node2,Node3
Node2.left = Node4
Node3.left,Node3.right = Node5,Node6
Node4.right = Node7
print instance.hasPathSum(Node1,26)

