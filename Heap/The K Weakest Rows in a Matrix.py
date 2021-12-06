# _*_ coding: utf-8 _*_
"""
# @Time : 12/5/2021 5:09 PM
# @Author : byc
# @File : The K Weakest Rows in a Matrix.py
# @Description :
"""
import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = dict()
        for i, row in enumerate(mat):
            key = sum(row)
            if key in d:
                d[key].append(i)
            else:
                d[key] = [i]
        heap = list(d.keys())
        heapq.heapify(heap)
        weakest = []
        while len(weakest) < k:
            if heap:
                vals = d[heapq.heappop(heap)]
                while vals:
                    if len(weakest) < k:
                        weakest.append(vals.pop(0))
                    else: break
        return weakest