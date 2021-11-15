# _*_ coding: utf-8 _*_
"""
# @Time : 11/14/2021 6:42 PM
# @Author : byc
# @File : Rotate List.py
# @Description :
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = head
        length = 0
        while tmp:
            length += 1
            tmp = tmp.next
        if length == 0: return head
        i = length - k % length
        first_head = head
        for i in range(i-1):
            head = head.next
        first_tail = head
        head = head.next
        second_head = second_tail = head
        while head:
            second_tail = head
            head = head.next
        if second_tail:
            second_tail.next = first_head
            first_tail.next = None
            return second_head
        else:
            return first_head