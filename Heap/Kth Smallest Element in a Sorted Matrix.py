# _*_ coding: utf-8 _*_
"""
# @Time : 12/5/2021 5:11 PM
# @Author : byc
# @File : Kth Smallest Element in a Sorted Matrix.py
# @Description :
"""
import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            heap += row
        heapq.heapify(heap)
        k = len(heap) if k > len(heap) else k
        return heapq.nsmallest(k, heap)[-1]
