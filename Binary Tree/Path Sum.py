# _*_ coding: utf-8 _*_
"""
# @Time : 11/17/2021 3:26 PM
# @Author : byc
# @File : Path Sum.py
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def findTarget(root, s):
            if not root: return False
            s += root.val
            if s == targetSum and not root.left and not root.right:
                return True
            return findTarget(root.left, s) or findTarget(root.right, s)
        return findTarget(root, 0)
