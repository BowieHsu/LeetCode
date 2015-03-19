#encoding:utf-8
__author__ = 'bowiehsu'
# Definition for singly-linked list.
import heapq
class ListNode:
     def __init__(self, x):
          self.val = x
          self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        #利用堆排序
        ras = []
        tail = head
        while tail:
            ras.append(tail.val)
            tail = tail.next
        heapq.heapify(ras)
        node = ListNode(0)
        tail2 = node
        while ras:
            node_proceed = ListNode(heapq.heappop(ras))
            tail2.next = node_proceed
            tail2 = tail2.next
        return node.next


instance = Solution()
node1,node2,node3 = ListNode(3),ListNode(2),ListNode(1)
node1.next , node2.next = node2,node3
head = instance.insertionSortList(node1)
while head:
    print head.val
    head = head.next
