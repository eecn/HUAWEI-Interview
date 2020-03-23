# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        # 本来应该import OrderedDict 以建立关键字按照创建顺序的字典
        # 默认的字典初始化也可以实现
        if len(s) == 0: return -1
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic.keys():
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1