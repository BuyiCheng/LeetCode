# _*_ coding: utf-8 _*_
"""
# @Time : 11/12/2021 4:58 PM
# @Author : byc
# @File : Linked List Cycle.py
# @Description :
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        low, fast = head.next, head.next.next
        while True:
            if low and fast:
                if low == fast:
                    return True
                low = low.next
                fast = fast.next
                if fast:
                    fast = fast.next
            else:
                return False