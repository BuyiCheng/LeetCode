# _*_ coding: utf-8 _*_
"""
# @Time : 11/18/2021 10:17 PM
# @Author : byc
# @File : Populating Next Right Pointers in Each Node.py
# @Description :
"""
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = deque([root])
        while q:
            length = len(q)
            for i in range(length):
                e = q.popleft()
                if q and i != length - 1:
                    e.next = q[0]
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)

        return root