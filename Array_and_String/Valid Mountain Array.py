# _*_ coding: utf-8 _*_
"""
# @Time : 10/17/2021 11:17 PM
# @Author : byc
# @File : Valid Mountain Array.py
# @Description :
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2: return False
        i = 0
        while i < len(arr) - 1:
            if arr[i] >= arr[i + 1]:
                break
            i += 1
        if i == 0 or i == len(arr) - 1:
            return False
        while i < len(arr) - 1:
            if arr[i] <= arr[i + 1]:
                break
            i += 1
        return i == len(arr) - 1
        # if len(arr) <= 2: return False
        # if arr[1] < arr[0]:
        #     return False
        # change_t, flag = 0, 1
        # for i in range(1, len(arr)):
        #     offset = arr[i] - arr[i-1]
        #     if offset == 0:
        #         return False
        #     elif offset > 0 and flag == 1:
        #         continue
        #     elif offset > 0 and flag == -1:
        #         change_t += 1
        #         flag = 1
        #     elif offset < 0 and flag == 1:
        #         change_t += 1
        #         flag = -1
        #     elif offset < 0 and flag == -1:
        #         continue
        # if change_t == 1:
        #     return True
        # return False

