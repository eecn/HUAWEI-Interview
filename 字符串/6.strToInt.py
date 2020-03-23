# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        length = len(s)
        if length == 0:
            return 0
        else:
            minus = False
            flag = False
            if s[0] == '+':
                flag = True
            if s[0] == '-':
                flag = True
                minus = True
            begin = 0
            if flag:
                begin = 1
            num = 0
            minus = -1 if minus else 1
            for each in s[begin:]:
                if each >= '0' and each <= '9':
                    num = num * 10 + minus * (ord(each) - ord('0'))
                else:
                    num = 0
                    break
            if num < -pow(2,31) or num>pow(2,31)-1:# python没有数字大小限制
                return 0
            return num