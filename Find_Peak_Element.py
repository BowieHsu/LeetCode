__author__ = 'bowiehsu'
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if num == None:
            return None
        l = sorted(num)
        return num.index(l[-1])

instance = Solution()
r = instance.findPeakElement([3,1])
print r