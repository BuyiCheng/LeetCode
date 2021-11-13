# _*_ coding: utf-8 _*_
"""
# @Time : 11/12/2021 4:59 PM
# @Author : byc
# @File : Intersection of Two Linked Lists.py
# @Description :
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = len_b = 0
        tmp_a, tmp_b = headA, headB
        while tmp_a:
            len_a += 1
            tmp_a = tmp_a.next
        while tmp_b:
            len_b += 1
            tmp_b = tmp_b.next
        if len_a < len_b:
            for i in range(len_b-len_a):
                headB = headB.next
        elif len_a > len_b:
            for i in range(len_a-len_b):
                headA = headA.next
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None