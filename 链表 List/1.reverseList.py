# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        # 特殊情况 空表或者只有一个结点的链表
        if not pHead  or not pHead.next:
            return pHead
        # 设置三个指针 分别指向当前节点的前一个节点、当前节点以及当前节点的下一个节点
        # 每次将当前节点的next指向其前一个节点
        pre = None
        pNode = pHead
        while pNode:
            pNext = pNode.next
            pNode.next = pre
            pre = pNode
            pNode = pNext
        return pre