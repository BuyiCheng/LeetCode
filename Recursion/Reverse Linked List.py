# _*_ coding: utf-8 _*_
"""
# @Time : 10/29/2021 9:54 PM
# @Author : byc
# @File : Reverse Linked List.py
# @Description :
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tmp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tmp
