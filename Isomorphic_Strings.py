#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        iso = {}
        iso2 = {}
        chas = []
        chat = []
        for i in s:
            chas.append(i)
        for j in t:
            chat.append(j)
        for i in range(len(chas)):
            iso[chas[i]] = chat[i]
            iso2[chat[i]] = chas[i]
        #print chat
        #print iso2
        res = ('').join(map(lambda x:iso[x],chas))
        res2 = ('').join(map(lambda x:iso2[x],chat))
        #print res
        return True if res == t and res2 == s else False

instance = Solution()
print instance.isIsomorphic("ab","aa")