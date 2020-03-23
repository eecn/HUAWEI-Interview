# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        dict = {}
        lis = []
        for elem in array:
            if elem in dict:
                dict[elem] += 1
            else:
                dict[elem] = 1
        for key,value in dict.items():
            if value == 1:
                lis.append(key)
        return lis