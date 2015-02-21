__author__ = 'bowiehsu'
class Solution:
    def trailingZeroes(self, n):
        return  0 if n < 5 else n/5 + self.trailingZeroes(n/5)

instance = Solution()
print 8/5
print instance.trailingZeroes(500)
