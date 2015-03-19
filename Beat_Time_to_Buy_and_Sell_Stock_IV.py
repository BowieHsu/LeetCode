#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @return an integer as the maximum profit
    def maxProfit(self,k,prices):
        #思想是求第二次卖出之后的最大值
        hold = [-65535]*k
        profit = [0]*k
        for i in prices:
            while k:
                #记录下每次的买入和卖出
                #依次比较
                profit[k-1] = max(profit[k-1], hold[k-1]+i)
                hold[k-1] = max(hold[k-1],-i)

                k -= 1
        return profit

instance = Solution()
prices = [1,2,3,4,5]
print instance.maxProfit(2,prices)
