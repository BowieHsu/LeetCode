#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        ras = [[0 for i in range(m+1)]for j in range(n+1)]
        ras[0][1] = 1
        print ras
        for v in range(1,n+1):
                for u in range(1,m+1):
                    if obstacleGrid[v-1][u-1] == 0:
                        ras[v][u] =ras[v-1][u]+ras[v][u-1]
                    #障碍物所在的状态置为0
                print ras,u,v
        return ras[n][m]


instance = Solution()
ob = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
ob2 = [[0,0],[1,1],[0,0]]
print instance.uniquePathsWithObstacles(ob)