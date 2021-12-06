# _*_ coding: utf-8 _*_
"""
# @Time : 12/5/2021 5:07 PM
# @Author : byc
# @File : Top K Frequent Elements.py
# @Description :
"""
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        for e in nums:
            if e in frequency:
                frequency[e] += 1
            else: frequency[e] = 1
        d = dict()
        for key,v in frequency.items():
            if v in d:
                d[v].append(key)
            else: d[v] = [key]
        heap = [-key for key in d.keys()]
        heapq.heapify(heap)
        result = []
        while True:
            if len(heap) > 0:
                key = heapq.heappop(heap)
                v_list = d[-key]
                while len(result) < k:
                    if v_list:
                        result.append(v_list.pop())
                    else:
                        break
            else:
                break
        return result