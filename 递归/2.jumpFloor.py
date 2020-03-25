# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number<3:
            return number
        first,second,third = 1, 2, 0
        for i in range(3,number+1):
            third = first+second
            first = second
            second = third
        return third