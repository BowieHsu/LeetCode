__author__ = 'bowiehsu'
class Solution:
    def generate(self,numRows):
        n,m = numRows,0
        A,out = [],[[]]
        while m < numRows:
            A.append(1)
            out.append(A)
            for i in range(1,m):
                A[i] += A[i-1]
                out[m][i] = A[i]
            m += 1
        return out
instance = Solution()
print instance.generate(5)
print range(1,5)