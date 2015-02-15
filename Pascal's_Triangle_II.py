__author__ = 'bowiehsu'
class Solution:
    def generate(self,rowIndex):
        out= [[1]]
        #print range(1,1)
        for l in range(1,rowIndex+1):
            out.append([1])
            for i in range(1,l):
               out[l].append(out[l-1][i]+out[l-1][i-1])
            #print A
            out[l].append(1)
        return out[rowIndex]
instance = Solution()
print instance.generate(0)
#print range(1,5)