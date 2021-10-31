# _*_ coding: utf-8 _*_
"""
# @Time : 10/30/2021 4:59 PM
# @Author : byc
# @File : Maximum Depth of Binary Tree.py
# @Description :
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #     def __init__(self):
    #         self.max_depth = 0
    #     def maxDepth(self, root: Optional[TreeNode]) -> int:
    #         self.recur(root, 0)
    #         return self.max_depth

    #     def recur(self, root, depth):
    #         if not root:
    #             if self.max_depth < depth:
    #                 self.max_depth = depth
    #             return
    #         depth += 1
    #         self.recur(root.left, depth)
    #         self.recur(root.right, depth)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1