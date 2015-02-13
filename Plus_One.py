__author__ = 'bowiehsu'
class Solution:
    def plusOne(self,digits):
        l = len(digits)
        num = 0
        for v in range(l):
            num += digits[v]*pow(10,l-v-1)
        num += 1
        return [int(i) for i in str(num)]

instance = Solution()
print instance.plusOne([1,2,3,4,5,6])