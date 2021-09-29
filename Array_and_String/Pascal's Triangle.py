# _*_ coding: utf-8 _*_
"""
# @Time : 9/29/2021 10:25 AM
# @Author : byc
# @File : Pascal's Triangle.py
# @Description :
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = list()
        for i in range(numRows):
            tmp_l = list()
            for e_i in range(i+1):
                if e_i == 0 or e_i == i:
                    tmp_l.append(1)
                else:
                    pre_layer = result[-1]
                    if len(pre_layer) > 1:
                        tmp_l.append(pre_layer[e_i-1]+pre_layer[e_i])
            result.append(tmp_l)
        return result