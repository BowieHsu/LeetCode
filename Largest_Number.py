#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        if sum(num) == 0:
            return "0"
        xl = len(num)
        ras = self.compare("",num,0,xl)
        return ras
    def compare(self,x,num,l,xl):
        if l == xl:
            return x
        y = str(num[l])
        #print y,l,num[l]
        return self.compare(max(x+y,y+x),num,l+1,xl)
instance = Solution()
A =[3, 30, 34, 5, 9]
#B = [1,2]
A = [9051,5526,2264,5041,1630,5906,6787,8382,4662,4532,6804,4710,4542,2116,7219,8701,8308,957,8775,4822,396,8995,8597,2304,8902,830,8591,5828,9642,7100,3976,5565,5490,1613,5731,8052,8985,2623,6325,3723,5224,8274,4787,6310,3393,78,3288,7584,7440,5752,351,4555,7265,9959,3866,9854,2709,5817,7272,43,1014,7527,3946,4289,1272,5213,710,1603,2436,8823,5228,2581,771,3700,2109,5638,3402,3910,871,5441,6861,9556,1089,4088,2788,9632,6822,6145,5137,236,683,2869,9525,8161,8374,2439,6028,7813,6406,7519]
#A = [121,12]
A =[0,9,8,7,6,5,4,3,2,1]
ras = instance.largestNumber(A)
print ras