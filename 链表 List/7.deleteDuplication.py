# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        h = ListNode(0)
        h.next = pHead
        pre = h
        cur = pHead
        while cur:
            if cur.next and cur.next.val == cur.val:
                tmp = cur.next
                while tmp and tmp.val == cur.val:
                    tmp = tmp.next
                pre.next = tmp
                cur = tmp
            else:
                pre = cur
                cur = cur.next
        return h.next
                    