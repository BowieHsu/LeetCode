__author__ = 'bowiehsu'
class Solution:
    def path(self,m,n):
        ras = []
        for i in range(m):
            ras.append(1)
        for v in range(n-1):
            for u in range(m-1):
                ras[u+1] =ras[u+1]+ras[u]
                '''
                if u == 0 and v == 0 :
                    ras [u+1] = 0
                elif u == 1 and v == 0:
                    ras [u+1] = 0
                '''
                print ras,u,v
        return ras[m-1]

instance = Solution()
print instance.path(3,3)