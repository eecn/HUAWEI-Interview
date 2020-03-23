# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        # 使用双指针
        lens = 0
        node = head
        while node:
            lens += 1
            node = node.next
        if k<1 or lens<k:
            return None
        right = head
        left = head
        for i in range(k-1):
            right = right.next
        while right.next:
            right = right.next
            left = left.next
        return left