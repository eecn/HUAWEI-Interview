# -*- coding:utf-8 -*-
def binary_search(lis,key):
    low = 0
    high = len(lis) - 1
    times = 0
    while low<=high:
        times += 1
        mid = (high+low) // 2
        if key == lis[mid]:
            print(times)
            return mid
        elif key > lis[mid]:
            low = mid + 1
        else:
            high = high - 1
    return None