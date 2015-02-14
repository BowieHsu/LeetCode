#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    def generateMatrix(self,n):
        trans,out = [],[]
        for i in range(n):
            out.append(range(n))
        #print out
        trans.extend(range(1,n**2+1))
        l,j,i = 0,0,0
        box,boy,upx,upy = 0,0,n-1,n-1
        while box <= upx and boy <= upy:
          #向右
          while j < upy and i == box:
             out[i][j] = trans[l]
             l += 1
             j += 1
          box += 1
          #向下
          while j == upy and i < upx:
             out[i][j] = trans[l]
             i += 1
             l += 1
          upy -= 1
          #向左
          while i == upx and j > boy:
             print l
             out[i][j] = trans[l]
             j -= 1
             l += 1
          upx -= 1
          #向上
          while j == boy and i > box :
             out[i][j] = trans[l]
             i -= 1
             l += 1
          boy += 1
          #每次单向移动完之后修改边界条件，由于界定条件原因，最后一个值单独赋
          out[i][j] = trans[l]
        return out

insatcne = Solution()
print insatcne.generateMatrix(3)