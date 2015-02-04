__author__ = 'bowiehsu'
#encoding = utf8
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        output,output2 = [],[]
        if root:
            temp = [root]
        else:
            return output2
        output2.append(temp)
        while True:
            #BSF
            for i in temp:
                if i.left:
                    output.append(i.left)
                if i.right:
                    output.append(i.right)
            if output == []:
                break
            output2.append(output)
            temp = list(output)
            output = []
        return [[v.val for v in x]for x in output2]


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