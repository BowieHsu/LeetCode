#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
     # @return an integer
    def totalNQueens(self, n):
        state = ()
        return len(list(self.queens(state,n)))

    #定义冲突
    def conflict(self,state,Nextx):
        Nexty = len(state)
        for i in range(Nexty):
            if abs(state[i]-Nextx) in (0,Nexty-i):
                return True
        return False
    #计算N皇后
    def queens(self,state,n):
        for i in range(n):
            #不冲突
            if not self.conflict(state,i):
                 #最后一个皇后
                 if len(state) == n-1:
                     yield (i,)
                 #回溯所有不冲突的方案
                 else:
                     for ans in self.queens(state+(i,),n):
                         yield (i,)+ans

instance = Solution()
print instance.totalNQueens(8)