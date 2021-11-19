# _*_ coding: utf-8 _*_
"""
# @Time : 11/18/2021 10:16 PM
# @Author : byc
# @File : Construct Binary Tree from Preorder and Inorder Traversal.py
# @Description :
"""
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder or not inorder:
        #     return
        # root_val = preorder.pop(0)
        # mid = inorder.index(root_val)
        # root = TreeNode(root_val)
        # root.left = self.buildTree(preorder, inorder[:mid])
        # root.right = self.buildTree(preorder, inorder[mid+1:])
        # return root
        d = dict([(v, k) for k, v in enumerate(inorder)])
        def recur(head, tail):
            if head > tail: return
            root_val = preorder.pop(0)
            mid = d[root_val]
            root = TreeNode(root_val)
            root.left = recur(head, mid-1)
            root.right = recur(mid+1, tail)
            return root
        return recur(0, len(inorder)-1)