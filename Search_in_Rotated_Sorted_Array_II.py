#encoding:utf=8
__author__ = 'bowiehsu'
class Solution:
    def search(self,A,target):
        if A == []:
            return -1
        else:
            #对于没有重复元素的有序翻转数列，可以通过判断mid和end元素的大小来判断其翻转情况
            l = len(A)
            index = 0
            tar = []
            if A[(l-1)/2] > A[-1]:
                if target < A[(l-1)/2]:
                    #二分搜索
                    tar = A[:(l-1)/2]
                else:
                    #继续递归
                    self.search(A[(l-1)/2:],target)
                    index += (l-1)/2
            else:
                if target < A[(l-1)/2]:
                    #继续递归
                    self.search(A[:(l-1)/2],target)
                else:
                    tar = A[(l-1)/2:]
                    index += (l-1)/2
            print tar
            high,low = len(tar)-1,0
            while high != low:
                mid = (high+low)/2
                if target <= tar[mid]:
                    high = mid
                else:
                    low = mid+1
            return high+index

instance = Solution()
r = [4,5,6,7,0,1,2]
try:
    return r.index(10)
except(ValueError):
    return -1
print r.index(10)

