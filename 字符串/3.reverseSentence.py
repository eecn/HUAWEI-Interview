# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s_list = s.split(' ')
        return ' '.join(s_list[::-1])