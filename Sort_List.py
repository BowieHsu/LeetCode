#encoding:utf-8
__author__ = 'bowiehsu'
# Definition for singly-linked list.
import heapq
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class TreeNode:
     def __init__(self,x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None:
            return None
        #构造一个堆
        tail = head
        ras = []
        while tail:
            ras.append(tail.val)
            tail = tail.next
        heapq.heapify(ras)
        out = ListNode(0)
        tail = out
        while ras:
            node = ListNode(heapq.heappop(ras))
            tail.next = node
            tail = tail.next
        return out.next


