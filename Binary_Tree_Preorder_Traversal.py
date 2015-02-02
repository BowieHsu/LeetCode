__author__ = 'bowiehsu'
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self,root):
        output = []
        if root != None:
             output.append(root.val)
             output.extend(self.preorderTraversal(root.left))
             output.extend(self.preorderTraversal(root.right))
        return output

instance = Solution()
root1 = TreeNode(1)
root2 = TreeNode(2)
root1.left = root2
r= instance.inorderTraversal(root1)
print r