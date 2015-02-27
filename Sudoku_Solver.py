#encoding:utf-8
import time
t0=time.time()
__author__ = 'bowiehsu'
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        #传入board
        self.board = board
        self.solved()
        t1=time.time()
        useTime=t1-t0
        print('\nuse Time: %f s'%(useTime))
        return board

    #寻找未知的点
    def find(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row,col
        return -1,-1

    #搜寻未知点的数字
    def solved(self):
        row,col = self.find()
        if row == -1 and col == -1:
            return True
        for num in ["1","2","3","4","5","6","7","8","9"]:
            if self.test(row,col,num):
               # print row,col,num
                a = list(self.board[row])
                a[col] = num
                self.board[row] = ''.join(a)
                #backtracking
                if self.solved():
                    return True
                a = list(self.board[row])
                a[col] = "."
                self.board[row] = ''.join(a)
        return False

    #判断该数字是否符合条件
    def test(self,row,col,num):
        srow = row - row%3
        scol = col - col%3
        if self.testcol(row,col,num) and self.testrow(row,col,num) and self.testsquare(srow,scol,num):
            return True
        return False

    #搜索行元素是否有重复
    def testrow(self,row,col,num):
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True

    #搜索列元素是否有重复
    def testcol(self,row,col,num):
        for j in range(9):
            if self.board[row][j] == num:
                return False
        return True

    #搜索3*3格子元素是否有重复
    def testsquare(self,srow,scol,num):
        for i in range(srow,srow+3):
            for j in range(scol,scol+3):
                if self.board[i][j] == num:
                    return False
        return True

instance = Solution()
board = ["..974....","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
diffcult = ["8........","..36.....",".7..9.2..",".5...7...","....457..","...1...3.","..1....68","..85...1.",".9....4.."]
board2 = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
for i in instance.solveSudoku(board2):
    print i

