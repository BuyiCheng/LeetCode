# _*_ coding: utf-8 _*_
"""
# @Time : 10/24/2021 8:14 PM
# @Author : byc
# @File : Closest Binary Search Tree Value.py
# @Description :
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_node, min_diff = root, abs(root.val-target)
        while True:
            if root is None:
                break
            else:
                diff = abs(root.val-target)
                if diff < min_diff:
                    min_diff = diff
                    min_node = root
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return min_node.val