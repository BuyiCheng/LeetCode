# _*_ coding: utf-8 _*_
"""
# @Time : 11/7/2021 8:55 PM
# @Author : byc
# @File : Binary Tree Level Order Traversal.py
# @Description :
"""


# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            tmp = []
            length = len(q)
            for _ in range(length):
                e = q.popleft()
                tmp.append(e.val)
                if e.left: q.append(e.left)
                if e.right: q.append(e.right)
            result.append(tmp)
        return result
