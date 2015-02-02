__author__ = 'bowiehsu'
# encoding=utf8
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a booleanclass Solution:
    # @param root, a tree node
    # @return a boolean

    def isSymmetric(self, root):
        return self.testSymmetric(root,root)

    def testSymmetric(self,root1,root2):
        #如果两个子均是空，为真
        if not root1 and not root2:
            return True
        #一个是空另外一个不是，或者两者的值不相等，为假
        elif not root1 or not root2 or root1.val != root2.val:
            return False
        return self.testSymmetric(root1.left,root2.right) and self.testSymmetric(root1.right,root2.left)
