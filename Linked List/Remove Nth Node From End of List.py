# _*_ coding: utf-8 _*_
"""
# @Time : 11/12/2021 5:00 PM
# @Author : byc
# @File : Remove Nth Node From End of List.py
# @Description :
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head, head_prev = head, None
        if not head: return None
        tail = head
        for i in range(n-1):
            tail = tail.next
        while tail.next:
            tail = tail.next
            head_prev = head
            head = head.next
        if not head_prev:
            return head.next
        head_prev.next = head.next
        return new_head