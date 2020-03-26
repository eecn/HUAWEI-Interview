# -*- coding:utf-8 -*-
def insert_sort(numbers):
    for i in range(len(numbers)-1):
        curNum,preIndex = numbers[i+1],i
        while preIndex>=0 and curNum<numbers[preIndex]:
            numbers[preIndex+1] = numbers[preIndex]
            preIndex = preIndex -1
        numbers[preIndex+1] = curNum
    return numbers