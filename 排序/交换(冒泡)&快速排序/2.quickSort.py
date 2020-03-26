# -*- coding:utf-8 -*-
def quickSort(numbers):
    if len(numbers)<=1:
        return numbers
    pivot = numbers[0]
    left = [numbers[i] for i in range(1,len(numbers)) if numbers[i] <= pivot]
    right = [numbers[j] for j in range(1,len(numbers)) if numbers[j] > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

def qiuckSortII(numbers,left,right):
    def partition(numbers,left,right):
        pivot = numbers[left]
        while left < right:
            while left<right and numbers[right] >= pivot:
                right-=1
            numbers[left] = numbers[right]
            while left<right and numbers[left] < pivot:
                left+=1
            numbers[right] = numbers[left]
            numbers[left] = pivot
        return left
    if left < right:
        pivotIndex = partition(numbers,left,right)
        qiuckSortII(numbers,left,pivotIndex)
        qiuckSortII(numbers,pivotIndex+1,right)
    return numbers