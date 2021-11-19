# _*_ coding: utf-8 _*_
"""
# @Time : 11/19/2021 11:12 AM
# @Author : byc
# @File : Binary Search Tree Iterator.py
# @Description :
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.l = []
        self.p = 0

        def traversal(root):
            if not root: return
            traversal(root.left)
            self.l.append(root.val)
            traversal(root.right)

        traversal(root)

    def next(self) -> int:
        if self.hasNext():
            p = self.p
            self.p += 1
            return self.l[p]

    def hasNext(self) -> bool:
        if self.p < len(self.l):
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()