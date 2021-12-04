# _*_ coding: utf-8 _*_
"""
# @Time : 12/3/2021 8:40 PM
# @Author : byc
# @File : Balanced Binary Tree.py
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def subBalanced(root):
            if not root:
                return True, 0
            left_balanced, left_height = subBalanced(root.left)
            right_balanced, right_height = subBalanced(root.right)
            height = max(left_height, right_height) + 1
            balanced = abs(left_height-right_height)<=1 and left_balanced and right_balanced
            return balanced, height
        balanced, _ = subBalanced(root)
        return balanced