# _*_ coding: utf-8 _*_
"""
# @Time : 11/12/2021 5:02 PM
# @Author : byc
# @File : Remove Linked List Elements.py
# @Description :
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head:
            if head.val == val:
                head = head.next
            else: break
        if not head: return None
        tail = head
        while tail.next:
            if tail.next.val == val:
                tail.next = tail.next.next
            else: tail = tail.next
        return head