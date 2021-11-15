# _*_ coding: utf-8 _*_
"""
# @Time : 11/14/2021 6:40 PM
# @Author : byc
# @File : Flatten a Multilevel Doubly Linked List.py
# @Description :
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def flattenSub(head):
            tail = head
            if not head:
                return head, tail
            prev_tail = None
            while tail:
                if tail.child:
                    sub_head, sub_prev_tail = flattenSub(tail.child)
                    sub_prev_tail.next = tail.next
                    if tail.next:
                        tail.next.prev = sub_prev_tail
                    tail.next = sub_head
                    sub_head.prev = tail
                    tail.child = None
                    tail = sub_prev_tail
                prev_tail = tail
                tail = tail.next
            return head, prev_tail

        head, _ = flattenSub(head)
        return head
