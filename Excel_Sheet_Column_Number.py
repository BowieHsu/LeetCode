__author__ = 'bowiehsu'
class Solution:
    #@param s ,a string
    #@return an integer
    def titleToNumber(self,s):
        "The code is really beautiful"
        return reduce(lambda x , y : 26*x+y , [ord(c)-64 for c in list(s)])


instance=Solution()
instance.titleToNumber("BA")

