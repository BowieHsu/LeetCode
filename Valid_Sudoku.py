#encoding:utf-8
__author__ = 'bowiehsu'
temp = 1<<9
row = 0
#print temp
class Solution:
    def isValidSudoku(self, board):
        if board == None:
            return False
        row = [0]*9
        col = [0]*9
        squ = [0]*9
       #以此遍历格子中已有的数字，判断sudoku是否合理
       #判断采用按位与的方式
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    print row,col,squ
                    occ = 1 << int(board[i][j])
                    ind = (i/3)*3 + j/3
                    #如果该数字在横、纵、3*3格子出现过，则为非法数字
                    if row[i] & occ or col[j]&occ or squ[ind]&occ:
                        return False
                    else:
                        row[i] = row[i]|occ
                        col[j] = col[j]|occ
                        squ[ind] = squ[ind]|occ

        return True


instance = Solution()
row,test = [0]*9,1<<9
row[0] = row[0] | test
#row= [0 for i in range(9)]
#ras = row[3] & test
#print row,ras
print instance.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])