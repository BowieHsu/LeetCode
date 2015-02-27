#encoding:utf-8
__author__ = 'bowiehsu'
# Definition for singly-linked list.
import heapq
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        #建堆将lists存入，利用堆排序输出链表
        if not lists:
            return None
        q = []
        head = ListNode(0)
        for i in lists:
            if i:
                q.append((i.val,i))
        #建堆
        heapq.heapify(q)
        tail = head
        while q:
            small,node = heapq.heappop(q)
            tail.next = node
            tail = node
            if node.next == None:
                continue
            heapq.heappush(node.next.val,node,next)
        return head.next


instance = Solution()
Node1,Node2,Node3,Node4 = ListNode(1),ListNode(2),ListNode(3),ListNode(4)
Node1.next,Node3.next = Node2,Node4
test = [{},{-1,5,11},{},{6,10}]
test1 = [{}]
mid = len(test)/2
forth,back = test[:mid],test[mid:]
print mid,forth,back
#print test1[:mid]== None
print instance.mergeKLists(test)
#print instance.helper(Node1,Node3)