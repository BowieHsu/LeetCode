#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    def permute(self,num):
        if len(num) <= 1:
            return [num]
        ras = []
        for idx,ele in enumerate(num):
            for elemt in self.permute(num[:idx]+num[idx+1:]):
                ras.append([ele]+elemt)
        return ras

instance = Solution()
r = [1,2,3]
out = instance.permute(r)
print out
u = [1,2,3]
print u[0:1]+u[2:]