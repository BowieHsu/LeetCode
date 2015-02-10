__author__ = 'bowiehsu'
class Solution:
    def grayCode(self,n):
        if n < 1: return [0,]
        if n == 1: return [0,1]
        bit = 1 << n-1
        lower = self.grayCode(n-1)
        return lower + [(bit|i)for i in reversed(lower)]
instance = Solution()
print instance.grayCode(3)