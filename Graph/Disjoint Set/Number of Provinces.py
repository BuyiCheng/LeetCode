# _*_ coding: utf-8 _*_
"""
# @Time : 12/8/2021 5:01 PM
# @Author : byc
# @File : Number of Provinces.py
# @Description :
"""
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         root = [i for i in range(len(isConnected))]
#         for i in range(len(isConnected)):
#             for j in range(i+1, len(isConnected[0])):
#                 if isConnected[i][j] == 0:
#                     continue
#                 if root[i] != root[j]:
#                     val = root[j]
#                     for r in range(len(root)):
#                         if root[r] == val:
#                             root[r] = root[i]
#         return len(set(root))
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected[0])):
                if isConnected[i][j] == 0:
                    continue
                if root[i] != root[j]:
                    val = root[j]
                    root[j] = root[i]
        count = 0
        for r in range(len(root)):
            if r == root[r]:
                count += 1
        return count