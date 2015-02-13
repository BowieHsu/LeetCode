__author__ = 'bowiehsu'
class Solution:
    def spiralOrder(self,matrix):
        out = matrix
        trans = []
        i,j = 0,0
        m,n = len(matrix),len(matrix[0])
        for v in matrix:
            trans += v
        while j < m and i == 0:
             out[i][j] = trans[]
             j += 1
             #break

        return out

insatcne = Solution()
r = [[1,2,3],[4,5,6],[7,8,9]]
print insatcne.spiralOrder(r)