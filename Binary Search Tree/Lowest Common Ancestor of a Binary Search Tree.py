# _*_ coding: utf-8 _*_
"""
# @Time : 12/1/2021 9:16 PM
# @Author : byc
# @File : Lowest Common Ancestor of a Binary Search Tree.py
# @Description :
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(root, node, path):
            if not root: return []
            path.append(root)
            new_path = path[:]
            if root.val == node.val:
                return path
            elif root.val > node.val:
                path = findPath(root.left, node, new_path)
            else:
                path = findPath(root.right, node, new_path)
            return path

        p_path = findPath(root, p, [])
        q_path = findPath(root, q, [])
        prev = p_path[0]
        i = 0
        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            prev = p_path[i]
            i += 1
        return prev
