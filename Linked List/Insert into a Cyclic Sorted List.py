# _*_ coding: utf-8 _*_
"""
# @Time : 11/14/2021 6:41 PM
# @Author : byc
# @File : Insert into a Cyclic Sorted List.py
# @Description :
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        n = Node(insertVal)
        if not head:
            head = n
            head.next = head
            return head

        new_head = head.next
        while new_head:
            if new_head == head:
                n.next = head.next
                head.next = n
                break
            cur_val, next_val = new_head.val, new_head.next.val
            if (cur_val <= insertVal <= next_val) or (
                    cur_val > next_val and (cur_val < insertVal or insertVal < next_val)):
                n.next = new_head.next
                new_head.next = n
                break
            new_head = new_head.next
        return head
