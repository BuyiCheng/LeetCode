# _*_ coding: utf-8 _*_
"""
# @Time : 11/12/2021 4:59 PM
# @Author : byc
# @File : Linked List Cycle II.py
# @Description :
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        low, fast = head.next, head.next.next
        first, second = head, None
        while True:
            if low and fast:
                if low == fast:
                    second = low
                    break
                else:
                    low = low.next
                    fast = fast.next
                    if fast:
                        fast = fast.next
            else:
                return None
        while first != second:
            first = first.next
            second = second.next
        return first