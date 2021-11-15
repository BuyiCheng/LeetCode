# _*_ coding: utf-8 _*_
"""
# @Time : 11/15/2021 1:48 PM
# @Author : byc
# @File : Binary Tree Preorder Traversal.py
# @Description :
"""


# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l = [root.val]
        l += self.preorderTraversal(root.left)
        l += self.preorderTraversal(root.right)
        return l
