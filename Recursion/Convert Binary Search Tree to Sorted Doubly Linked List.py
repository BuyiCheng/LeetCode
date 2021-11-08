# _*_ coding: utf-8 _*_
"""
# @Time : 11/7/2021 8:56 PM
# @Author : byc
# @File : Convert Binary Search Tree to Sorted Doubly Linked List.py
# @Description :
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        n_list = list()
        if not root: return None
        def traverse(root):
            if not root:
                return
            if root.left:
                traverse(root.left)
            n_list.append(root)
            if root.right:
                traverse(root.right)
        traverse(root)
        length = len(n_list)
        if length == 1:
            root.left = root
            root.right = root
            return root
        for i in range(length):
            if i == 0:
                n_list[i].left = n_list[length-1]
                n_list[i].right = n_list[i+1]
            elif i == length-1:
                n_list[i].right = n_list[0]
                n_list[i].left = n_list[i-1]
            else:
                n_list[i].left = n_list[i-1]
                n_list[i].right = n_list[i+1]
        return n_list[0]