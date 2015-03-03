__author__ = 'bowiehsu'
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        if S == []:
            return S
        ls = len(S)
        ras,ras2= [[]],[]
        S.sort()
        for i in range(ls):
            #ras.append([S[i]])
            cur = len(ras)
            for j in range(len(ras)-cur,len(ras)):
                ras.append(ras[j]+[S[i]])
                #print i,j,ras[j]+[S[i]],len(ras)-cur,len(ras),cur
        #return ras
        ras.sort()
        ras2.append(ras[0])
        for i in range(len(ras)-1):
            #print i,i+1
            if ras[i] != ras[i+1]:
                ras2.append(ras[i+1])
        return ras2


instance = Solution()
print instance.subsetsWithDup([1,2,3])