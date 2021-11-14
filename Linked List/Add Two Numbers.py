# _*_ coding: utf-8 _*_
"""
# @Time : 11/14/2021 2:39 PM
# @Author : byc
# @File : Add Two Numbers.py
# @Description :
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        next_val = 0
        prev_l1 = None
        while l1 and l2:
            s_val = l1.val + l2.val + next_val
            l1.val, next_val = s_val % 10, s_val // 10
            prev_l1 = l1
            l1 = l1.next
            l2 = l2.next
        if l2:
            prev_l1.next = l2
            l1 = l2
        while l1:
            prev_l1 = l1
            s_val = l1.val + next_val
            l1.val, next_val = s_val % 10, s_val // 10
            l1 = l1.next
        if next_val != 0:
            prev_l1.next = ListNode(next_val)
        return head
