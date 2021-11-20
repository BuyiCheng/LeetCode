# _*_ coding: utf-8 _*_
"""
# @Time : 11/20/2021 2:23 PM
# @Author : byc
# @File : Delete Node in a BST.py
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val == key:
            return self.delete(root)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

    def delete(self, root):
        if root.left and root.right:
            successor = root.right
            if not successor.left:
                successor.left = root.left
                return successor
            prev_succ = successor
            while successor.left:
                prev_succ = successor
                successor = successor.left
            prev_succ.left = successor.right
            successor.left, successor.right = root.left, root.right
            return successor
        if not root.left and not root.right:
            return None
        else:
            return root.left if root.left else root.right