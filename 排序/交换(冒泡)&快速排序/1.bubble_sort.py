# -*- coding:utf-8 -*-
def bubbleSort(numbers):
    for i in range(len(numbers)-1):
        swap = False
        for j in range(len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
                swap = True
        if not swap:
            break
    return numbers