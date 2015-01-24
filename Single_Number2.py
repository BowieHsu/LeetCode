__author__ = 'bowiehsu'
class Solution:
    def singleNumber(self,A):
        A=sorted(A)
        buf=[]
        l=len(A)
        for i in range(l-1) :
            if A[i] == A[i+1]:
                buf.append(A[i])
        return int(sum(A)-sum(buf)*1.5)

instance = Solution()
r = instance.singleNumber([1,1,1,2,2,2,3])
print r
