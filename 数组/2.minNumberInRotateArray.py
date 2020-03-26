# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        # left指向前面的递增数组 right指向后面的递增数组
        left = 0
        right = len(rotateArray) - 1
        mid = 0
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                mid = right
                break
            mid = left + (right - left) // 2
            if rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
                return self.minInorder(rotateArray, left, right)
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
        return rotateArray[mid]
    
    def minInorder(self, array, left, right):   ##顺序查找
        result = array[left]
        for i in range(left+1, right+1):
            if array[i] < result:
                result = array[i]
        return result