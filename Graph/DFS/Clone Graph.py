# _*_ coding: utf-8 _*_
"""
# @Time : 12/24/2021 7:12 PM
# @Author : byc
# @File : Clone Graph.py
# @Description :
"""

# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        nodes = {node.val: Node(node.val)}
        stack = deque([node])
        while stack:
            length = len(stack)
            for i in range(length):
                e = stack.popleft()
                nbs = e.neighbors
                for n in nbs:
                    if n.val not in nodes:
                        nodes[n.val] = Node(n.val)
                        stack.append(n)
                    nodes[e.val].neighbors.append(nodes[n.val])
                print(e.val, [i.val for i in nodes[e.val].neighbors])
        return nodes[node.val]

