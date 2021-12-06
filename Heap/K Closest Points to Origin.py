# _*_ coding: utf-8 _*_
"""
# @Time : 12/5/2021 5:13 PM
# @Author : byc
# @File : K Closest Points to Origin.py
# @Description :
"""
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = dict()
        for i, p in enumerate(points):
            d = (p[0]**2+p[1]**2)**0.5
            if d in dist:
                dist[d].append(i)
            else:
                dist[d] = [i]
        heap = list(dist.keys())
        heapq.heapify(heap)
        closest = []
        while len(closest) < k:
            indices = dist[heapq.heappop(heap)]
            while indices:
                if len(closest) < k:
                    closest.append(points[indices.pop()])
                else: break
        return closest