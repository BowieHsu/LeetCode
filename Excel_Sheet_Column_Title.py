#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @return a string
    def convertToTitle(self, num):
        if num == 0:
            return None
        if num > 65536:
            num = long(num)
        ras =""
        dic = ["Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]

        while num:
            #print num
            #print num,(num)%26,dic[24]
            ras=dic[(num)%26]+ras
            num -= 1
            num /= 26
        return ras

instance = Solution()
print instance.convertToTitle(52)