# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 0:
            return 0
        maxSum = array[0]
        curSum = array[0]
        
        for each in array[1:]:
            if curSum <= 0:
                curSum = each
            else:
                curSum += each
            if curSum > maxSum:
                maxSum = curSum
        return maxSum