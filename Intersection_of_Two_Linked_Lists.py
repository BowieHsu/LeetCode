__author__ = 'bowiehsu'
#encoding:utf-8
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        head1,head2 = headA,headB
        numa,numb = 0,0
        if head1 == None or head2 == None:
            return None
        #既然A和B有公共部分且有序，
        # 那么只要将A和B的长度缩减一致，必能在相互的next范围内找到公共点
        while head1.next:
            numa += 1
            head1 = head1.next
        while head2.next:
            numb += 1
            head2 = head2.next
        head1,head2 = headA,headB
        print head1.val,head2.val,numa,numb
        if numa > numb:
            for i in range(numa-numb):
                head1 = head1.next
        else:
            for i in range(numb-numa):
                head2 = head2.next
        print head1.val,head2.val
        while head1 != head2 and head1:
            head1 = head1.next
            head2 = head2.next
        return head1

instance = Solution()
node1 = ListNode(1)
node2,node3,node4 = ListNode(2),ListNode(3),ListNode(4)
node1.next,node2.next,node3.next = node3,node3,node4
node5,node6,node7 = ListNode(5),ListNode(6),ListNode(5)
node6.next = node7
print instance.getIntersectionNode(node5,node6)
