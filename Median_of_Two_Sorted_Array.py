#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        ras = A+B
        if m == 0 or n == 0:
            if (m+n)%2 != 0:
                return float(ras[(m+n)/2])
            else:
                return (float(ras[(m+n)/2])+float(ras[(m+n)/2-1]))/2
                #return out
        while m and n:
               #print m,n
               if A[m-1] > B[n-1]:
                 ras[m+n-1] = A[m-1]
                 m = m-1
               else:
                 ras[m+n-1] = B[n-1]
                 n = n-1
        ras[:n] = B[:n]
        m,n =len(A),len(B)
        if (m+n)%2 != 0:
                return float(ras[(m+n)/2])
        else:
                #print (float(ras[(m+n)/2])+float(ras[(m+n)/2-1]))/2
                return (float(ras[(m+n)/2])+float(ras[(m+n)/2-1]))/2

instance = Solution()
A = [1,2,3,4,5]
B = [7,8,9,10]
print instance.findMedianSortedArrays([2,3],[2,3])
