# _*_ coding: utf-8 _*_
"""
# @Time : 10/31/2021 4:24 PM
# @Author : byc
# @File : Validate Binary Search Tree.py
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(root, -math.inf, math.inf)

    def validBST(self, root, min_v, max_v):
        if not root: return True
        if min_v < root.val < max_v:
            isleft = self.validBST(root.left, min_v, root.val)
            isright = self.validBST(root.right, root.val, max_v)
            if isleft and isright:
                return True
        return False
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         self.prev = -math.inf
#         return self.inorder(root)

#     def inorder(self, root):
#         if not root:
#             return True
#         if not self.inorder(root.left):
#             return False
#         if root.val <= self.prev:
#             return False
#         self.prev = root.val
#         if not self.inorder(root.right):
#             return False
#         return True