# _*_ coding: utf-8 _*_
"""
# @Time : 9/30/2021 8:25 PM
# @Author : byc
# @File : Pascal's Triangle II.py
# @Description :
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = [1]
        for i in range(1, rowIndex + 2):
            pre = 1
            for j in range(i):
                if j == 0:
                    l[j] = 1
                elif j == i - 1:
                    l.append(1)
                else:
                    tmp = l[j]
                    l[j] = pre + l[j]
                    pre = tmp

        return l