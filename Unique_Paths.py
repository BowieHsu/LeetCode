__author__ = 'bowiehsu'
class Solution:
    def path(self,m,n):
        ras = []
        for i in range(m):
            ras.append(1)
        for v in range(n-1):
            for u in range(m-1):
                ras[u+1] =ras[u+1]+ras[u]
        return ras[m-1]

instance = Solution()
print instance.path(2,4)
print range(10)