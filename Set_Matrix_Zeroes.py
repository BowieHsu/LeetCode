# encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    def setZeroes(self,matrix):
        col,row= [],[]
        if matrix == []:
            return []
        m,n = len(matrix[0]),len(matrix)
        for inx,ele in enumerate(matrix):
            for ind,v in enumerate(ele):
                if v == 0:
                #记录0元素出现的行数和列数
                    row.append(inx)
                    col.append(ind)
        print row,col
        #将含有0的行全部置0
        for i in row:
            matrix[i] = m*[0]
        #将含有0的列全部置0
        for j in col:
            for r in matrix:
               r[j] = 0
        return matrix

instance = Solution()
r = [[1,2,3],[4,0,6],[7,8,9]]
r2 = [[1]]
r3 =[[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
print instance.setZeroes(r)
