__author__ = 'bowiehsu'
#encoding:utf-8
class Solution:
    def wordBreak(self,s,dict):
        temp = ""
        ras = []
        if(self.test(s,dict) == False):
            return ras
        self.helper(s,0,dict,temp,ras)
        return ras

    def helper(self,s,length,dict,temp,ras):
        if length >= len(s):
            ras.append(temp[0:len(temp)-1])
            return ras

        for i in range(length,len(s)):
            if s[length:i+1] in dict:
                self.helper(s,i+1,dict,temp+s[length:i+1]+" ",ras)

# 确定该string是否由dictionary组成
    def test(self,s,dict):
        ls = len(s)
        rs = [False]*ls
        for i in range(len(s)):
            for w in dict:
                #print s,w
                if s[i-len(w)+1:i+1] == w and (rs[i-len(w)] or i-len(w)==-1):
                    rs[i] = True
        return rs[-1]
instance = Solution()
s = "catsanddog"
dict = ["sand","dog","cat","cats","and","catsanddog"]
print instance.wordBreak(s,dict)
