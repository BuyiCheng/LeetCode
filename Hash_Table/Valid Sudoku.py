# _*_ coding: utf-8 _*_
"""
# @Time : 10/16/2021 7:35 PM
# @Author : byc
# @File : Valid Sudoku.py
# @Description :
"""
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = defaultdict(list)
        h, w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] != '.':
                    m['r' + str(i)].append(board[i][j])
                    m['c' + str(j)].append(board[i][j])
                    m['b' + str(i // 3) + str(j // 3)].append(board[i][j])
        for v in m.values():
            if len(v) != len(set(v)):
                return False
        return True
