#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == []:
            return []
        trans,out = [],[]
        m,n = len(matrix[0]),len(matrix)
        #print out
        l,j,i = 0,0,0
        box,boy,upx,upy = 0,0,n-1,m-1
        #只有一行
        if upx == 0 or upy == 0:
            for v in matrix:
                out.extend( v)
            return out
        while box <= upx and boy <= upy:
          #向右
          while j < upy:
             out.append(matrix[box][j])
             j += 1
          box += 1
          print j
          #向下
          while i < upx:
             out.append(matrix[i][upy])
             i += 1
          upy -= 1
          #向左
          while j > boy:
             out.append(matrix[upx][j])
             j -= 1
          upx -= 1
          print j
          #向上
          while i > box :
             out.append(matrix[i][boy])
             i -= 1
          boy += 1
          #每次单向移动完之后修改边界条件，由于界定条件原因，最后一个值单独赋
        #print len(out),m,n,j
        if len(out) < m*n:
           out.append(matrix[i][j])
        #print m,n
        #print box,boy,upx,upy
        return out

instance = Solution()
matrix2 =[[6,7,8,9,10]]
matrix3 = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print instance.spiralOrder(matrix)
