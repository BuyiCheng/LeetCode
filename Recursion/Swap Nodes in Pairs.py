# _*_ coding: utf-8 _*_
"""
# @Time : 10/29/2021 9:53 PM
# @Author : byc
# @File : Swap Nodes in Pairs.py
# @Description :
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp
