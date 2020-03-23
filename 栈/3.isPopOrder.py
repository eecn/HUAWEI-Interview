# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(popV) == 0 or len(pushV) != len(popV):
            return False
        stackData = []
        for i in pushV:
            stackData.append(i)
            while len(stackData) and stackData[-1] == popV[0]:
                stackData.pop()
                popV.pop(0)
        if len(stackData):
            return False
        return True