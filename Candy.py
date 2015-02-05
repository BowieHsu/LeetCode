__author__ = 'bowiehsu'
class Solution:
    def candy(self,ratings):
        candy = [1]
        l = len(ratings)-1
        for x in range(l):
            if(ratings[x] < ratings[x+1]):
                candy.append(candy[x]+1)
            else:
                candy.append(1)
        pl = range(l)
        for i in pl[l::-1]:
            if(ratings[i] > ratings[i+1]):
                candy[i] = max(candy[i],candy[i+1]+1)
        return sum(candy)

instance = Solution()
r = [4,2,3,4,1]
print instance.candy(r)
x = range(10)
print x
print x[10::-1]