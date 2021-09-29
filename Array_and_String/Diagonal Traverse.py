# _*_ coding: utf-8 _*_
"""
# @Time : 9/28/2021 8:38 PM
# @Author : byc
# @File : Diagonal Traverse.py
# @Description : ***
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = dict()
        for r in range(len(mat)):
            for c in range(len(mat[r])):
                if (r + c) not in d:
                    d[r+c] = [mat[r][c]]
                else:
                    d[r+c].append(mat[r][c])
        l = list()
        for k in d.keys():
            if k % 2 == 0:
                l.extend(d[k][::-1])
            else:
                l.extend(d[k])

        return l