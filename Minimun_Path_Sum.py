__author__ = 'bowiehsu'
class Solution:
    def minPathSum(self,grid):
        m = len(grid)
        n = len(grid[0])
        for u in range(1,m):
            grid[u][0] += grid[u-1][0]
        for v in range(1,n):
            grid[0][v] += grid[0][v-1]
        for u in range(1,m):
            for v in range(1,n):
                grid[u][v] += min(grid[u-1][v],grid[u][v-1])
        return grid[m-1][n-1]

instance = Solution()
r = [[1,2,3],[4,5,6],[7,8,9]]
out = instance.minPathSum(r)
print out