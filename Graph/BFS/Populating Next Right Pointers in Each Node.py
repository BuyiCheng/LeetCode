# _*_ coding: utf-8 _*_
"""
# @Time : 12/24/2021 7:14 PM
# @Author : byc
# @File : Populating Next Right Pointers in Each Node.py
# @Description :
"""
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        stack = deque([root])
        while stack:
            length = len(stack)
            for i in range(length):
                e = stack.popleft()
                if i < length-1:
                    e.next = stack[0]
                if e.left: stack.append(e.left)
                if e.right: stack.append(e.right)
        return root