__author__ = 'bowiehsu'
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def SumNumbers(self,root):
        return self.helper(root,0)

    def helper(self,root,sum):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return sum*10+root.val
        return self.helper(root.left,sum*10+root.val)+self.helper(root.right,sum*10+root.val)


instance = Solution()
node0 = TreeNode(20)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4,node5 = TreeNode(4),TreeNode(5)
node1.left,node1.right = node2,node3
node2.left,node2.right = node4,node5
print instance.SumNumbers(node1)