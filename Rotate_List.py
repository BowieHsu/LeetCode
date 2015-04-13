#encoding:utf-8
__author__ = 'bowiehsu'
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None:
            return None
        if k == 0 or head.next == None:
            return head
        tail = head
        cnt = 1
        #指针遍历整个链表，得到链表的长度
        while tail.next:
            tail = tail.next
            cnt += 1
        tail.next = head
        num = k%cnt
        num = cnt - num
        while num:
            tail = tail.next
            num -= 1
        res = tail.next
        tail.next = None
        return res

N1 = ListNode(1)
N2 = ListNode(2)
N3 = ListNode(3)
N4 = ListNode(4)
N5 = ListNode(5)
N1.next,N2.next,N3.next,N4.next = N2,N3,N4,N5
instance = Solution()
nod = instance.rotateRight(N1,0)
while nod:
    print nod.val
    nod = nod.next
