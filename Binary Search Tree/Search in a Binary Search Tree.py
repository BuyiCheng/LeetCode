# _*_ coding: utf-8 _*_
"""
# @Time : 11/20/2021 2:21 PM
# @Author : byc
# @File : Search in a Binary Search Tree.py
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while True:
            if not root or root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left
#         if not root:
#             return None
#         elif root.val == val:
#             return root
#         elif root.val < val:
#             return self.searchBST(root.right, val)
#         else:
#             return self.searchBST(root.left, val)
