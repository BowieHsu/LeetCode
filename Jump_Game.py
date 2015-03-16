#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        path = 1
        return self.helper(path,0,A)

    def helper(self,path,i,A):
        path += A[i]
        print path
        if path < len(A):
            if A[i] == 0:
                return False
            else:
                return self.helper(path,path,A)
        else:
            return True


instance = Solution()
A = [2,0,1,1,4]
B = [3,2,1,0,4]
print instance.canJump(A)