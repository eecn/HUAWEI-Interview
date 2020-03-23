# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        res = []
        l = len(array)
        for i in range(l):
            # 从后往前 奇数的话 添加到前面 则是按原来的顺序
            if array[l-i-1] % 2 != 0:
                res.insert(0,array[-i-1])
            if array[i] % 2 == 0:
                # 由后往前 偶数的话 则在后面添加
                res.append(array[i])
        return res