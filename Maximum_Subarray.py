__author__ = 'bowiehsu'

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubarray(self,A):
        value,buf=-65536,0
        for i in A:
            buf = max(i,buf+i)
            value = max(value,buf)
        return value

instance = Solution()
r = instance.maxSubarray([-1,-2])
print r
