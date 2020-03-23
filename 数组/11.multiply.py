# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        if len(A) == 0:
            return B
        else:
            for i in range(len(A)):
                tmp = A[i]
                A[i] = 1
                B.append(reduce(lambda x,y: x*y,A))
                A[i] = tmp
        return B
                         