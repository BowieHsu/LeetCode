__author__ = 'bowiehsu'
class Solution:
    def merge(self,A,m,B,n):
       while m and n:
           if A[m-1]>B[n-1]:
                A[m+n-1],m,n = A[m-1],m-1,n
           else:
                A[m+n-1],m,n = B[n-1],m,n-1
       #以下这行如何理解
       A[:n] = B[:n]
       return A

instance = Solution()
print instance.merge([],4,[1],1)