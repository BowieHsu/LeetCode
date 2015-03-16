#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    def hammingWeight(self, n):
        bi = []
        #print n
        while n:
            bi = bi + [n%2]
            n = n/2
            print bi,n
        l = 0
        for i in bi:
            #print l,n
            if i != 0:
                l += 1
        return l


instance = Solution()
n = 19
print instance.hammingWeight(n)