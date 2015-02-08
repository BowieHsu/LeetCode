#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    def permute(self,num):
      #依次交换位置
        ras,num2 = [num],[]
        l = len(num)-1
        for x in num:
            num2.append(x)
        for y in range(l):
            num2[y],num2[y+1] = num2[y+1],num2[y]
        ras.append(num2)
        return ras

instance = Solution()
r = [1,2,3]
out = instance.permute(r)
print out