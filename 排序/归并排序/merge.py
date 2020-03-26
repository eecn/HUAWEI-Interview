# -*- coding:utf-8 -*-
def mergeSort(numbers):
    def merge(left,right):
        result = []
        i=j=0
        while i <len(left) and j<len(right):
            if left[i]<=right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:]
        return result
    if len(numbers) <= 1:
        return numbers
    mid  = len(numbers) // 2
    left = mergeSort(numbers[:mid])
    right = mergeSort(numbers[mid:])
    return merge(left,right)
    
