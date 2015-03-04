#encoding:utf-8
__author__ = 'bowiehsu'
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    #克隆一个二叉树
    def clone(self,n):
        if n == None:
            return None
        new = TreeNode(n.val)
        new.left = self.clone(n.left)
        new.right = self.clone(n.right)
        return new

    # @return a list of tree node
    def generateTrees(self, n):
        if n == 0:
            return []
        ras = [TreeNode(1)]
        for i in range(2,n+1):
            temp = []
            for j in range(len(ras)):
                #以new为root节点
                old = ras[j]
                target = self.clone(old)
                new = TreeNode(i)
                new.left = target
                temp.append(new)
                #print temp[j].val
                #以i-1为root节点，以此遍历，new应该为目前节点的右子树，原节点的右子树为new的左子树
                if old :
                    tem = old
                    while tem.right:
                        nonroot = TreeNode(i)
                        tright = tem.right
                        nonroot.left = tem.right
                        tem.right = nonroot
                        target = self.clone(old)
                        temp.append(target)
                        tem.right = tright
                        tem = tem.right
                        print j,target.val,tem.val
                    #old的右子树为空时，依然需要添加new为目前节点的右子树
                    tem.right = TreeNode(i)
                    target = self.clone(old)
                    temp.append(target)
            ras = temp
        ras.sort()
        return ras


'''
    #构建一个二叉搜索树
    def build(self,T,n):
        if T == None:
            T = n
        x = T
        while x:
            y = x
            if n.val < x.val:
                x = x.left
            else:
                x = x.right
        if n.val < y.val:
            y.left = n
        else:
            y.right = n
        return T
'''
instance = Solution()
'''
node1 = TreeNode(3)
node1.left,node1.right = TreeNode(1),TreeNode(4)
node2 = TreeNode(2)
ras = instance.build(node1,node2)
ras2 = instance.clone(ras)
'''
result = instance.generateTrees(4)
'''
for i in result:
    print i.val
'''
#test =[{1,#,2,#,3,#,4},{1,#,2,#,4,3},{1,#,3,2,4},{1,#,4,2,#,#,3},{1,#,4,3,#,2},{2,1,3,#,#,#,4},{2,1,4,#,#,3},{3,1,4,#,2},{3,2,4,1},{4,1,#,#,2,#,3},{4,1,#,#,3,2},{4,2,#,1,3},{4,3,#,1,#,#,2},{4,3,#,2,#,1}]


