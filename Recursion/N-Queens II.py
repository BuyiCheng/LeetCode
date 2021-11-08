# _*_ coding: utf-8 _*_
"""
# @Time : 11/7/2021 8:50 PM
# @Author : byc
# @File : N-Queens II.py
# @Description :
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diagonals, anti_diagonals):
            if row == n:
                return 1

            count = 0
            for col in range(n):
                diag = row - col
                anti_diag = row + col
                if col in cols or diag in diagonals or anti_diag in anti_diagonals:
                    continue
                cols.append(col)
                diagonals.append(diag)
                anti_diagonals.append(anti_diag)
                count += backtrack(row + 1, cols, diagonals, anti_diagonals)
                cols.remove(col)
                diagonals.remove(diag)
                anti_diagonals.remove(anti_diag)
            return count

        return backtrack(0, [], [], [])