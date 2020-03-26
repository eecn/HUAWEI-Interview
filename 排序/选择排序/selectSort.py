# -*- coding:utf-8 -*-
def selectSort(numbers):
    for i in range(len(numbers)-1):
        minIndex = i
        for j in range(i+1,len(numbers)):
            if numbers[j] < numbers[minIndex]:
                minIndex = j
            numbers[i],numbers[minIndex] = numbers[minIndex],numbers[i]
    return numbers

                
            