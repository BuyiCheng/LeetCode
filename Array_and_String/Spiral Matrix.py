# _*_ coding: utf-8 _*_
"""
# @Time : 9/28/2021 10:00 PM
# @Author : byc
# @File : Spiral Matrix.py
# @Description :
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        directions = ['right', 'down', 'left', 'up']
        dd = {'right': (0, 1), 'down': (1, 0), 'left': (0, -1), 'up': (-1, 0)}

        r_s, r_e, c_s, c_e = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        s = [0, 0]
        l = [matrix[s[0]][s[1]]]
        di = 0

        while r_s <= r_e and c_s <= c_e:
            d = dd[directions[di]]
            r, c = s[0] + d[0], s[1] + d[1]
            if r_s <= r <= r_e and c_s <= c <= c_e:
                s = [r, c]
                l.append(matrix[r][c])
            else:
                if di < len(directions) - 1:
                    di += 1
                else:
                    di = 0
                if directions[di] == 'right':
                    c_s += 1
                elif directions[di] == 'left':
                    c_e -= 1
                elif directions[di] == 'down':
                    r_s += 1
                elif directions[di] == 'up':
                    r_e -= 1

        return l