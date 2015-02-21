#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        #将所有的字符按空格符分离
        #将其中不是空格符的元素存入out,返回out中的最后一个元素的长度
            out = []
            s = s.split(' ')
            print s
            print s[-1]
            for i in s:
                if i != '':
                    out.append(i)
            if out == []:
                return 0
            print out
            return len(list(out[-1]))


instance = Solution()
r = "Hello World"
r2 = ""
r3 = "b     "
print instance.lengthOfLastWord(r2)