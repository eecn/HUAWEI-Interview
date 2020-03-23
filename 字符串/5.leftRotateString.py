# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        length = len(s)
        if n <= 0 or length == 0:
            return s
        if n > length:
            n = n % length
        return s[n:] + s[:n]