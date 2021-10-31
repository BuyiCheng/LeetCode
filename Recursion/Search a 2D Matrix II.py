# _*_ coding: utf-8 _*_
"""
# @Time : 10/31/2021 4:25 PM
# @Author : byc
# @File : Search a 2D Matrix II.py
# @Description :
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = m-1, 0
        while row >=0 and col < n:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else: return True
        return False