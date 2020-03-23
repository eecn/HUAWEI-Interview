# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 思路：  使用快慢指针 找到换中的节点
        #        统计环的长度
        #        使用两个指针 找到环的入口节点
        if pHead == None:
            return None
        meetingnode = self.MeetingNode(pHead)
        if meetingnode == None:
            return None
        nodeslop = 1
        node1 = meetingnode
        while node1.next != meetingnode:
            node1 = node1.next
            nodeslop += 1
        node1 = pHead
        for _ in range(nodeslop):
            node1 = node1.next
        node2 = pHead
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next
        return node1
        
    def MeetingNode(self, pHead):
        if not pHead:
            return None
        slow = pHead
        fast = slow.next
        while fast != None:
            if slow == fast:
                return fast
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
        return None
