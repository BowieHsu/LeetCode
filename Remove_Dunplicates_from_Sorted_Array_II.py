__author__ = 'bowiehsu'
class Solution:
    def removeDulicates(self,A):
        l = len(A)
        out = []
        #for ind,ele in enumerate(A):
        #print range(2,l)
        for v in range(2,l):
            if A[v] == A[v-1] and A[v] == A[v-2]:
                out.append(v)
        if out != []:
            out.reverse()
            for i in out:
                A.remove(A[i])
        return A
instance = Solution()
r = [1,1,1,1]
print instance.removeDulicates(r)