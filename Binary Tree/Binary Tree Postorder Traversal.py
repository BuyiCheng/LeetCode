# _*_ coding: utf-8 _*_
"""
# @Time : 11/15/2021 1:49 PM
# @Author : byc
# @File : Binary Tree Postorder Traversal.py
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        if not root: return l
        l += self.postorderTraversal(root.left)
        l += self.postorderTraversal(root.right)
        l.append(root.val)
        return l
