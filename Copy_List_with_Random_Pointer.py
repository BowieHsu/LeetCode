#encoding:utf-8
__author__ = 'bowiehsu'
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution:
    def copyRandomList(self,head):
        