__author__ = 'bowiehsu'
class Solution:
    def trailingZeroes(self, n):
        num = self.generate(n)
        out = list(str(num))
        out.sort()
        ras = 0
        for i in out:
            if i == '0':
                ras += 1
        return ras
    def generate(self,n):
        if n == 0:
            return 1
        else:
            return n*self.generate(n-1)

instance = Solution()
print instance.generate(500)
