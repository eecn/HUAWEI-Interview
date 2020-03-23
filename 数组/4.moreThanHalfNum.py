# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        '''
        # 字典的方法
        dict = {}
        lens = len(numbers)
        if lens == 0:
            return 0
        for i in range(lens):
            if numbers[i] in dict.keys():
                dict[numbers[i]] += 1
            else:
                dict[numbers[i]] = 1
        for i in list(dict.keys()):
            if dict[i] > lens //2:
                return i
        return 0
        '''
        result = numbers[0]
        times = 1
        for i in range(1, len(numbers)):
            if times == 0:
                result = numbers[i]
                times = 1
            elif result == numbers[i]:
                times += 1
            else:
                times -= 1
        times = 0
        for i in range(len(numbers)):
            if numbers[i] == result:
                times += 1
        return result if times > len(numbers) // 2 else 0

                    