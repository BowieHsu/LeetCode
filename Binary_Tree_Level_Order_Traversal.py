__author__ = 'bowiehsu'
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        output = []
        output2 = []
        if root != None:
             output.append(root.val)
           #  output2.extend(root.left.val)
           #  output2.extend(root.right.val)
             self.levelOrder(root.left)
             self.levelOrder(root.right)
            # output.append(output2)
             #output2.extend(self.levelOrder(root.left))
             #output2.extend(self.levelOrder(root.right))
        return output

instance = Solution()
root1 = TreeNode(1)
root2 = TreeNode(2)
root3 = TreeNode(3)
root4 = TreeNode(4)
root5 = TreeNode(5)
root1.left,root1.right = root2,root3
root2.left,root2.right = root4,root5
r = instance.levelOrder(root1)
print r