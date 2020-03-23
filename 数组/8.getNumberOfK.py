# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)
        '''
        if not data:
            return 0
        low, lens = 0, len(data)-1
        high = lens
        if k<data[low] or k>data[high]:
            return 0
        while low<=high:
            mid = (high + low) //2
            if k==data[mid]:
                left = mid
                while(left>=0 and k==data[left]):
                    left -= 1
                left += 1
                right = mid
                while(right<=lens and data[right] == k):
                    right += 1
                right -= 1
                return right- left + 1
            elif k<data[mid]:
                high = mid-1
            else:
                low = mid+1
        return 0
        '''
