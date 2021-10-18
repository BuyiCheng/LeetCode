# _*_ coding: utf-8 _*_
"""
# @Time : 10/17/2021 11:16 PM
# @Author : byc
# @File : Check If N and Its Double Exist.py
# @Description :
"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        m = dict()
        for e in sorted(arr):
            if e in m.values():
                return True
            if e < 0:
                if e % 2 == 0:
                    m[e] = e / 2
            else:
                m[e] = e * 2
        return False
        # arr = sorted(arr)
        # center = 0
        # for i in range(1, len(arr)):
        #     if arr[i-1] < 0 and arr[i] >= 0:
        #         center = i
        #         break
        # arr_list = [[abs(e) for e in arr[:center]][::-1], arr[center:]]
        # for arr in arr_list:
        #     start, end = 0, 1
        #     while end < len(arr):
        #         if arr[end] == 2*arr[start]:
        #             return True
        #         elif arr[end] < 2*arr[start]:
        #             end += 1
        #         else:
        #             start += 1
        #             if start >= end:
        #                 end += 1
        # return False