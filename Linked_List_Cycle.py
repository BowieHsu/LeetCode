__author__ = 'bowiehsu'
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

instance = Solution()
Node1,Node2,Node3 = ListNode(1),ListNode(2),ListNode(3)
Node = ListNode(0)
head = ListNode(1)
Node.next,Node1.next,Node2.next = Node1,Node2,Node
r = instance.hasCycle(head)
print r
print Node