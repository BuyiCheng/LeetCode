# _*_ coding: utf-8 _*_
"""
# @Time : 11/17/2021 3:25 PM
# @Author : byc
# @File : Symmetric Tree.py
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right: return True
        def leftTree(root):
            if not root:
                return [None]
            l = [root.val]
            l += leftTree(root.left)
            l += leftTree(root.right)
            return l
        def rightTree(root):
            if not root: return [None]
            l = [root.val]
            l += rightTree(root.right)
            l += rightTree(root.left)
            return l
        left = leftTree(root.left)
        right = rightTree(root.right)
        if len(left) != len(right): return False
        else:
            for i in range(len(left)):
                if left[i] != right[i]:
                    return False
            return True