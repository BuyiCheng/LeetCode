# _*_ coding: utf-8 _*_
"""
# @Time : 11/20/2021 2:22 PM
# @Author : byc
# @File : Insert into a Binary Search Tree.py
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root: return node
        new_root = root
        while True:
            if root.val < val:
                if root.right:
                    root = root.right
                else:
                    root.right = node
                    break
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = node
                    break
        return new_root
