# _*_ coding: utf-8 _*_
"""
# @Time : 11/14/2021 6:41 PM
# @Author : byc
# @File : Copy List with Random Pointer.py
# @Description :
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        tmp = head
        count = 0
        m = dict()
        while tmp:
            m[tmp] = count
            count += 1
            tmp = tmp.next
        node_map = dict()
        for i in range(count):
            if i not in node_map:
                node_map[i] = Node(head.val)
            if head.next:
                if i+1 not in node_map:
                    node_map[i+1] = Node(head.next.val)
                node_map[i].next = node_map[i+1]
            random = head.random
            if random:
                if m[random] not in node_map:
                    node_map[m[random]] = Node(random.val)
                node_map[i].random = node_map[m[random]]
            head = head.next
        return node_map[0]