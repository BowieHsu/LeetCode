#encoding:utf-8
__author__ = 'bowiehsu'
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if nums == None or k == None:
            return None
        ras = []
        ls = len(nums)
        if ls < k:
            k = k%ls
        #print range(-1,-k-1,-1)
        print range(-k,0),range(ls-k)
        for i in range(-k,0):
            ras.append(nums[i])
        for j in range(ls-k):
            ras.append(nums[j])
        return ras

instance = Solution()
r = [1,2]
r1 = [-1]
print instance.rotate([1,2],1)