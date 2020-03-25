# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number<2:
            return number
        total = 1
        for i in range(1,number):
            total = 2*total
        return total