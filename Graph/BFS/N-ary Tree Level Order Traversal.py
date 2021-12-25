# _*_ coding: utf-8 _*_
"""
# @Time : 12/24/2021 7:15 PM
# @Author : byc
# @File : N-ary Tree Level Order Traversal.py
# @Description :
"""
from collections import deque
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return root
        q = deque([root])
        results = []
        while q:
            l = len(q)
            temp = []
            for _ in range(l):
                n = q.popleft()
                temp.append(n.val)
                for c in n.children:
                    q.append(c)
            results.append(temp)
        return results