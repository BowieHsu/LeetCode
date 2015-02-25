#encodng:utf-8
__author__ = 'bowiehsu'
class Solution:
    def solveNQueens(self, n):
        state = ()
        ras = []
        for solution in self.queen(n,state):
            temp2 = []
            for pos in solution:
                length = len(solution)
                temp = "."*pos +"Q"+"."*(length-pos-1)
                temp2.append(temp)
            ras.append(temp2)
        return ras

    def queen(self,n,state):
        for pos in range(n):
            if not self.conflict(state,pos):
                if len(state) == n-1:
                    yield (pos,)
                else:
                    for result in self.queen(n,state+(pos,)):
                        yield (pos,)+result
    def conflict(self,state,nextX):
        nextY = len(state)
        for i in range(nextY):
            if abs(state[i]-nextX) in (0, nextY-i):
                return True
        return False

instance = Solution()
print instance.solveNQueens(4)