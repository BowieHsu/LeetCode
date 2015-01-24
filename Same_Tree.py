__author__ = 'bowiehsu'
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def isSameTree(self,p,q):
        if p == None and q == None:
            return True
        elif (p and q) and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False