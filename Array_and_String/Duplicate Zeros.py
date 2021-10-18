# _*_ coding: utf-8 _*_
"""
# @Time : 10/17/2021 11:14 PM
# @Author : byc
# @File : Duplicate Zeros.py
# @Description :
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        length = len(arr)
        while i < length:
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 1
            i += 1
        rl = len(arr) - length
        for _ in range(rl):
            arr.pop()