__author__ = 'bowiehsu'
class Solution:
    #@return an integer
    def numTrees(self,n):
        if n==0 or n==1:
            return 1
        else:
            return sum((self.numTrees(n-1-i)*self.numTrees(i))for i in range(n))

instance=Solution()
r=instance.numTrees(4)
print r