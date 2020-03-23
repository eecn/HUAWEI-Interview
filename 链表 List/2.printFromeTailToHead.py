# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        # write code here
        head = listNode
        res = []
        while head:
            res.insert(0,head.val)
            head = head.next
        return res