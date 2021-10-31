# _*_ coding: utf-8 _*_
"""
# @Time : 10/30/2021 5:00 PM
# @Author : byc
# @File : Merge Two Sorted Lists.py
# @Description :
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2: return None
        elif not l1 and l2: return l2
        elif l1 and not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        # if not l1 and not l2: return None
        # elif not l1 and l2: return l2
        # elif l1 and not l2: return l1
        # head = tail = None
        # if l1.val <= l2.val:
        #     head = tail = l1
        #     l1 = l1.next
        #     tail.next = None
        # else:
        #     head = tail = l2
        #     l2 = l2.next
        #     tail.next = None
        # while not l1 or not l2:
        #     if l1.val <= l2.val:
        #         tail.next = l1
        #         tail = l1
        #         l1 = l1.next
        #         tail.next = None
        #     else:
        #         tail.next = l2
        #         tail = l2
        #         l2 = l2.next
        #         tail.next = None
        # while l1:
        #     tail.next = l1
        # while l2:
        #     tail.next = l2
        # return head