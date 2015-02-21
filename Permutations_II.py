#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    def permuteUnique(self,num):
        if num == None:
            return []
        trans = []
        l = len(num)
        num.sort()
        ret = [[]]
        #print range(2,-1,-1)
        #含有重复项的排列应该是每个元素和后面不相同的元素交换位置
        for i,n in enumerate(num):
          

          #print trans
          #print ind
        #print trans
        return ret

instance = Solution()
r = [1,1,1,2]
print instance.permuteUnique(r)