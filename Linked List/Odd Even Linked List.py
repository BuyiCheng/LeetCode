# _*_ coding: utf-8 _*_
"""
# @Time : 11/12/2021 5:03 PM
# @Author : byc
# @File : Odd Even Linked List.py
# @Description :
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        even_head = even_tail = head
        odd_head = odd_tail = head.next
        i = 2
        head = head.next.next
        while head:
            if i % 2 == 0:
                even_tail.next = head
                even_tail = head
            else:
                odd_tail.next = head
                odd_tail = head
            head = head.next
            i += 1
        if odd_head != head:
            odd_tail.next = None
            even_tail.next = odd_head
        return even_head