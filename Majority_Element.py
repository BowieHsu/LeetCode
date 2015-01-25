__author__ = 'bowiehsu'
class Solution:
    def majorityElement(self,num):
        num.sort()
        return num[len(num)/2]


instance = Solution()
r = instance.majorityElement([1,1,1,1,1,1,1,1,1,1])
print r

