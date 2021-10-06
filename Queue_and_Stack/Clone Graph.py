# _*_ coding: utf-8 _*_
"""
# @Time : 10/6/2021 12:52 PM
# @Author : byc
# @File : Clone Graph.py
# @Description :
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        adj = {}
        self.DFS(node, adj)
        node_d = {}
        for i in adj.keys():
            node_d[i] = Node(val=i)
        for v in node_d.values():
            v.neighbors = [node_d[i] for i in adj[v.val]]
        return node_d[1] if node else None

    def DFS(self, node, adj):
        if node is None or node.val in adj:
            return
        elif node.neighbors == None:
            adj[node.val] = []
            return
        adj[node.val] = [n.val for n in node.neighbors]
        for n in node.neighbors:
            self.DFS(n, adj)