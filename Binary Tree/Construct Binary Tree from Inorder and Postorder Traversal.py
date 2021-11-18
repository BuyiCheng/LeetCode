# _*_ coding: utf-8 _*_
"""
# @Time : 11/17/2021 4:28 PM
# @Author : byc
# @File : Construct Binary Tree from Inorder and Postorder Traversal.py
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d = dict([(v,k) for k,v in enumerate(inorder)])
        def recur(head, tail):
            if head > tail:
                return
            val = postorder.pop()
            root = TreeNode(val)
            mid = d[val]
            root.right = recur(mid+1, tail)
            root.left = recur(head, mid-1)
            return root
        return recur(0, len(inorder)-1)
#         if not inorder or not postorder:
#             return
#         val = postorder.pop()
#         root = TreeNode(val)
#         mid = inorder.index(val)
#         root.right = self.buildTree(inorder[mid+1:], postorder)
#         root.left = self.buildTree(inorder[:mid], postorder)

#         return root