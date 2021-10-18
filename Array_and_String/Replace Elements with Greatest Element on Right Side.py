# _*_ coding: utf-8 _*_
"""
# @Time : 10/17/2021 11:18 PM
# @Author : byc
# @File : Replace Elements with Greatest Element on Right Side.py
# @Description :
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        max_v = -1
        for i in range(len(arr) - 1, -1, -1):
            e = arr[i]
            arr[i] = max_v
            if e > max_v:
                max_v = e

        return arr