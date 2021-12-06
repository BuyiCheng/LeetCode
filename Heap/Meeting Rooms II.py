# _*_ coding: utf-8 _*_
"""
# @Time : 12/5/2021 5:12 PM
# @Author : byc
# @File : Meeting Rooms II.py
# @Description :
"""
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetings = sorted(intervals, key=lambda x: x[0])
        heap = []
        heapq.heapify(heap)
        for m in meetings:
            if len(heap) == 0:
                heapq.heappush(heap, m[1])
                continue
            if m[0] >= heap[0]:
                heapq.heappushpop(heap, m[1])
            else:
                heapq.heappush(heap, m[1])
        return len(heap)