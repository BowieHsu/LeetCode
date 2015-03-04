#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower()
        ras = list(s)
        ras2 = []
        if s == "":
            return True
        for i in ras:
            if i.isalnum() and not i.isspace():
                ras2.append(i)

        for i in range(len(ras2)/2):
            print ras2[i],ras2[len(ras2)-i-1]
            if ras2[i] != ras2[len(ras2)-i-1]:
                return False
        return True

instance = Solution()
s = "6A man, a plan, a c c anal: Panama6"
print instance.isPalindrome("")