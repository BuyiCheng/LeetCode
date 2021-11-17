# _*_ coding: utf-8 _*_
"""
# @Time : 11/17/2021 3:27 PM
# @Author : byc
# @File : Count Univalue Subtrees.py
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
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def isUnival(root):
            count = 0
            if not root:
                return True, 0
            isLeft, left_count = isUnival(root.left)
            isRight, right_count = isUnival(root.right)
            isUni = True
            if (root.left and root.left.val != root.val) or (root.right and root.right.val != root.val) or (not isLeft or not isRight):
                count = -1
                isUni = False
            count += 1
            return isUni, count + left_count + right_count
        _, c = isUnival(root)
        return c
