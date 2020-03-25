# -*- coding:utf-8 -*-
def  unOrder_search(lis,key):
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
    return  None