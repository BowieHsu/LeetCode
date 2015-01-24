__author__ = 'bowiehsu'
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self,head):
        if head == None:
            return None
        node = head
        while node.next:
          if node.val == node.next.val:
              node.next = node.next.next
          else:
              node = node.next
        return head

l1 = ListNode(1)
l2 = ListNode(2)
#l3 = ListNode(2)
l1.next = l2
#l2.next = l3
instance = Solution()
r=instance.deleteDuplicates(l1)
print r.val

