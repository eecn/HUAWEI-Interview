# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.Data = []
        self.Min = []
    def push(self, node):
        # write code here
        self.Data.append(node)
        if self.Min:
            if self.Min[-1] > node:
                self.Min.append(node)
            else:
                self.Min.append(self.Min[-1])   #保证Min栈的栈顶一直指向最小的数字，即使出现重复输入也不会出错
        else:
            self.Min.append(node)
    def pop(self):
        # write code here
        if self.Data == []:
            return None
        self.Min.pop()
        return self.Data.pop()
    def top(self):
        # write code here
        if self.Data == []:
            return None
        return self.Data[-1]
    def min(self):
        # write code here
        if self.Min == []:
            return None
        return self.Min[-1]