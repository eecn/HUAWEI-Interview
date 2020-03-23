# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or  not pHead2:
            return None
        len1, len2 = 0, 0
        node1 = pHead1
        node2 = pHead2
        # 思路 先找到比较长的链表 由于链表具有交叉节点，则从该节点向后的节点都相同
        # 所以先让一个指针走相差的长度数后，对比链表的节点值找到第一个相同的公共节点 包括val和next
        while node1:
            len1 += 1
            node1 = node1.next
        while node2:
            len2 += 1
            node2 = node2.next
        if len1 >= len2:
            longList = pHead1
            shortList = pHead2
        else:
            longList = pHead2
            shortList = pHead1
        
        dif = abs(len1-len2)
        for i in range(dif):
            longList = longList.next
        while longList !=  shortList  and longList != None:
            longList = longList.next
            shortList = shortList.next
            
        if longList:
            return longList
        return None # 没有公共节点的情况
            