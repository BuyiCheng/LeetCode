# _*_ coding: utf-8 _*_
"""
# @Time : 11/18/2021 10:19 PM
# @Author : byc
# @File : Lowest Common Ancestor of a Binary Tree.py
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
        if root == p or root == q:
            return root
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right
        # self.p_path = None
        # self.q_path = None
        # def findTarget(root, path):
        #     if not root: return
        #     path.append(root)
        #     if root == p:
        #         self.p_path = path[:]
        #     if root == q:
        #         self.q_path = path[:]
        #     if self.p_path and self.q_path:
        #         return
        #     findTarget(root.left, path)
        #     while path[-1]!= root:
        #         path.pop()
        #     findTarget(root.right, path)
        #     return path
        # findTarget(root, [])
        # lca = None
        # min_len = len(self.p_path) if len(self.p_path) < len(self.q_path) else len(self.q_path)
        # for _ in range(min_len):
        #     p_a, q_a = self.p_path.pop(0), self.q_path.pop(0)
        #     if p_a == q_a:
        #         lca = p_a
        #     else:
        #         break
        # return lca