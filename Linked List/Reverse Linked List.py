# _*_ coding: utf-8 _*_
"""
# @Time : 11/12/2021 5:01 PM
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

        if not head: return None
        tail = head
        while tail.next:
            new_head = tail.next
            tail.next = new_head.next
            new_head.next = head
            head = new_head
        return head

        # if not head or not head.next:
        #     return head
        # tmp = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return tmp

