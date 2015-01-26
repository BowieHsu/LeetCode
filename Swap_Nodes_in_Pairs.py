__author__ = 'bowiehsu'
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def swapPairs(self,head):
        p1 = guard = ListNode(0)
        guard.next = head
        try:
            while True:
                p0, p1, p2 = p1, p1.next, p1.next.next
                p0.next, p1.next, p2.next = p2, p2.next, p1
        except:
            return guard.next