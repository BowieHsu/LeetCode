#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    def wordBreak(self,s,dict):
        ls = len(s)
        rs = [False]*ls
        #rs[-1] = True
        for i in range(ls):
            for w in dict:
                print s[i-len(w)+1:i+1]
                if s[i-len(w)+1:i+1] == w and (rs[i-len(w)] or i-len(w) == -1):
                    rs[i] = True
        return rs


instance = Solution()
s = "leetcode"
dict = ["leet","code","lee"]
s2 = "aaaaaaa"
dict2 = ["aaaa","aa"]
print instance.wordBreak(s2,dict2)