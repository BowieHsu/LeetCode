#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        ras1 = [int(s) for s in version1.split(".")]
        ras2 = [int(s) for s in version2.split(".")]
        if int(ras1[0]) > int(ras2[0]):
            return 1
        elif int(ras1[0]) < int(ras2[0]):
            return -1
         #补0，避免两个数字的长度不相等的情况
        test1 = ras1[1:]+[0]*(max(len(ras1),len(ras2))-len(ras1))
        test2 = ras2[1:]+[0]*(max(len(ras1),len(ras2))-len(ras2))
        print test1,test2
        if test1 > test2:
           return 1
        elif test1 < test2:
            return -1
        return 0


instance = Solution()
v1 = "1.0"
v2 = "1.1"
r1,r2 = "10.6.5","10.6"
print len(v1),len(v2),v1+"0"*2
print instance.compareVersion(r1,r2)
