# _*_ coding: utf-8 _*_
"""
# @Time : 11/19/2021 11:11 AM
# @Author : byc
# @File : Inorder Successor in BST.py
# @Description :
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor