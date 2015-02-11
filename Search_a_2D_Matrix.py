__author__ = 'bowiehsu'
class Solution:
    def searchMatrix(self,matrix,target):
        l = len(matrix)
        m = len(matrix[0])
        tar = []
        for x in range(l):
            if target >= matrix[x][0] and target <= matrix[x][m-1]:
                tar = matrix[x]
        if tar == []:
            return None
        high,low = m-1,0
        while high > low:
            mid = (high+low)/2
            if target > tar[mid]:
                low = mid+1
            else:
                high = mid
        if target == tar[high]:
            return True
        else:
            return False

instance = Solution()
r = [[1,2,4],[5,6,7],[8,9,10]]
print instance.searchMatrix(r,3)

