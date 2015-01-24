__author__ = 'bowiehsu'
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
          high,low,mid = len(A)-1,0,len(A)/2
          while low < high:
            if target < A[mid]:
              low,high = low,mid-1
            elif target > A[mid]:
              low,high = mid,high
            else:
               return mid
            mid=(low+high+1)/2
          if target > A[mid]:
              return mid+1
          return mid
           #print "what the fuck?"


instance = Solution()
r = instance.searchInsert([1,3,4,5,6,10],)
#l=range(1,5)
#i = [1,3,5,7,9,2,4,6,8,10]
#print i,i[0:2],i[5:10]
print r
#print l
