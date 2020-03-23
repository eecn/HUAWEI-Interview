# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
       self.val = x
       self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        '''
        # 递归解法
        if not pHead1: return pHead2
        if not pHead2: return pHead1
        mergeHead = None
        if pHead1.val <= pHead2.val:
            mergeHead = pHead1
            mergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            mergeHead = pHead2
            mergeHead.next = self.Merge(pHead1, pHead2.next)
        return mergeHead
        '''
        
        # 循环解法
        
        # 先构造一个头节点以便代码简洁
        h = ListNode(-1)
        cur1 = pHead1
        cur2 = pHead2
        cur = h
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        if not cur1:
            cur.next = cur2
        if not cur2:
            cur.next = cur1
        return h.next

        
        