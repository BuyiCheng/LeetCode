# _*_ coding: utf-8 _*_
"""
# @Time : 10/7/2021 8:29 PM
# @Author : byc
# @File : Binary Tree Inorder Traversal.py
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        visited = set()
        self.inorder(root, result, visited)
        return result

    def inorder(self, cur, result, visited):
        if cur is None:
            return
        if cur.left:
            self.inorder(cur.left, result, visited)
        if cur.left is None or cur.left in visited:
            result.append(cur.val)
            visited.add(cur)
        if cur.right:
            self.inorder(cur.right, result, visited)