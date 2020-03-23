# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        '''
        # 暴力法 归并排序(没有理解透彻)
        cnt = 0
        for i in range(len(data)-1):
            for j in range(i+1,len(data)):
                if data[i]>data[j]:
                    cnt+=1
        return cnt%1000000007
        '''
        # 排序法 每次找到排序后的最小值 查看他在原数组中的位置，则它前面的数字和他构成逆序对
        copy = []
        for i in data:
            copy.append(i)
        copy.sort()
        cnt = 0
        for i in range(len(copy)):
            cnt += data.index(copy[i])
            data.remove(copy[i])
        return cnt%1000000007