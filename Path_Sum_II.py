#encoding:utf-8
__author__ = 'bowiehsu'
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        ras,path,i = [],[root.val],0
        self.hasPathSum(path,ras,root,sum)
        return ras

    def hasPathSum(self,path,ras,root, sum):
        if root.left:
               path.append(root.left.val)
               self.hasPathSum(path,ras,root.left,sum-root.val)
               path.pop()
        if root.right:
               path.append(root.right.val)
               self.hasPathSum(path,ras,root.right,sum-root.val)
               path.pop()
        if not root.right and not root.left:
            if sum-root.val != 0:
                return None
            else:
                ras.append(path[:])
                return ras

instance = Solution()
Node1,Node2,Node3,Node4,Node5,Node6,Node7,Node8,Node9,Node10 \
= TreeNode(5),TreeNode(4),TreeNode(8),TreeNode(11),\
  TreeNode(13),TreeNode(4),TreeNode(7),TreeNode(2),TreeNode(5),TreeNode(1)
Node1.left,Node1.right = Node2,Node3
Node2.left = Node4
Node3.left,Node3.right = Node5,Node6
Node4.left,Node4.right = Node8,Node7
Node6.left,Node6.right = Node9,Node10
#print instance.hasPathSum(Node1,26)
print instance.pathSum(Node1,22)