# _*_ coding: utf-8 _*_
"""
# @Time : 10/16/2021 7:36 PM
# @Author : byc
# @File : Find Duplicate Subtrees.py
# @Description :
"""


# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        m = defaultdict(int)
        tm = dict()
        tree = self.DFS(root, m, tm)
        result = []
        for k, v in m.items():
            if v > 1:
                result.append(tm[k])
        return result

    def DFS(self, node, hashmap, treemap):
        if node is None:
            return (None,)
        tree = (node.val,)
        left_tree = self.DFS(node.left, hashmap, treemap)
        right_tree = self.DFS(node.right, hashmap, treemap)
        tree += left_tree
        tree += right_tree
        hashmap[tree] += 1
        treemap[tree] = node
        return tree