#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    def isHappy(self,n):
        if n == 1:return True
        elif n == 0:return False
        m = set()
        while n not in m:
            m.add(n)
            n = self.Ji(n)
            if n == 1:return True
            #print n
        return False

    def Ji(self,n):
        buff = []
        out = 0
        while n != 0:
            a = n%10
            buff.append(a)
            n /= 10
        for i in buff:
            out += i**2
        return out

instance = Solution()
print instance.isHappy(3)