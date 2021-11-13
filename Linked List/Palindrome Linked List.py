# _*_ coding: utf-8 _*_
"""
# @Time : 11/12/2021 5:04 PM
# @Author : byc
# @File : Palindrome Linked List.py
# @Description :
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # if not head: return True
        # s = ''
        # while head:
        #     s += str(head.val)
        #     head = head.next
        # if s == s[::-1]:
        #     return True
        # return False
        def reverse(head):
            if not head: return head
            tail = head
            while tail.next:
                new_head = tail.next
                tail.next = new_head.next
                new_head.next = head
                head = new_head
            return head

        length = 0
        new_head = head
        while new_head:
            length += 1
            new_head = new_head.next
        half = int(length / 2 - 1 if length % 2 == 0 else length // 2)
        i = 0
        new_head = head
        while i < half - 1:
            new_head = new_head.next
            i += 1
        if length % 2 == 0:
            right_head = reverse(new_head.next)
        else:
            tmp = ListNode(new_head.val, new_head.next)
            right_head = reverse(tmp)
        for i in range(half + 1):
            if head.val != right_head.val:
                return False
            head = head.next
            right_head = right_head.next
        return True