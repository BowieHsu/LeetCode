#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if haystack == "" and needle == "":
            return 0
        elif haystack != "" and needle == "":
            return 0
        elif haystack == "" and needle == "":
            return -1
        m,n = len(haystack),len(needle)
        #print m,n,range(1)
        #对于needle是1个数字的情况还需要单独考虑
        if n == 1:
            for i in range(m):
                if haystack[i] == needle:
                    return i
            return -1
        for i in range(m-n+1):
            for j in range(n):
                print i,j
                if haystack[i+j] != needle[j]:
                    break
            #上述情况没办法验证最后一位，还需要对最后一位单独进行验证
            if j == n-1 and haystack[i+j] == needle[j]:return i
        return -1

instance = Solution()
haystack,needle = "mississippi", "issip"
print instance.strStr(haystack,needle)