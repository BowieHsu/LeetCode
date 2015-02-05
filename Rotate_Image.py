__author__ = 'bowiehsu'
class Solution:
    def rotate(self,matrix):
        m = len(matrix)
        out = []
        for i in range(m):
            mat = []
            for j in range(m):
               mat.append(matrix[j][i])
            mat.reverse()
            out.append(mat)
        matrix[i].reverse()
        return out

instance = Solution()
r = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
out = instance.rotate(r)
print out