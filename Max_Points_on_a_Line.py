#encoding:utf-8
__author__ = 'bowiehsu'
class Point:
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution:
    def maxPoint(self,points):
        #find the maximum number of points that lie on the same straight line
        #存储斜率
        l = len(points)
        if l == 1:
            return 1
        max_value = 0
        for ind,point in enumerate(points):
            repeat = 1
            dic = {}
            for others in points[ind+1:]:
                #设置不同的斜率
                if others.x == point.x  and point.y != others.y:
                    ratio = "infi"
                    if dic.has_key(ratio):
                        dic[ratio] += 1
                    else:
                        dic[ratio] = 1
                elif others.x == point.x  and others.y == point.y:
                    repeat += 1
                elif point.x != others.x:
                    ratio = float(point.y - others.y)/float(point.x - others.x)
                    if dic.has_key(ratio):
                        dic[ratio] += 1
                    else:
                        dic[ratio] = 1
            #根据每一个连线的斜率情况进行分类
            local_max = 0
            for value in dic.values():
                local_max = max(local_max,value)
            print dic
            local_max += repeat
            max_value = max(max_value,local_max)
        return max_value

instance = Solution()
point1 = Point(0,0)
point2 = Point(0,0)
point3 = Point(1,3)
point4 = Point(-1,-1)
point5 = Point(2,2)
data = [point1,point4,point5]
print instance.maxPoint(data)
