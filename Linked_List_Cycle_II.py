#encoding:utf-8
__author__ = 'bowiehsu'
#建立链表节点
class Listnode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self,head):
        if head == None:
            return None
        A,B,C = head,head,head
        while A.next and A.next.next:
            A = A.next.next
            B = B.next
            if A == B:
                #从起点出发和从汇合点出发的两个指针的交点就是cycle的起点
               while A != C:
                   A = A.next
                   C = C.next
               return C
        return None



