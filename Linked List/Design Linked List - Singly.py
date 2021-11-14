# _*_ coding: utf-8 _*_
"""
# @Time : 11/12/2021 4:56 PM
# @Author : byc
# @File : Design Linked List - Singly.py
# @Description :
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        tmp = self.head
        for i in range(index):
            if tmp:
                tmp = tmp.next
            else:
                return -1
        return tmp.val if tmp else -1

    def addAtHead(self, val: int) -> None:
        n = Node(val)
        n.next = self.head
        self.head = n

    def addAtTail(self, val: int) -> None:
        tmp = self.head
        n = Node(val)
        if tmp:
            while tmp.next:
                tmp = tmp.next
            tmp.next = n
        else:
            self.head = n

    def addAtIndex(self, index: int, val: int) -> None:
        if index != 0:
            tmp = self.head
            for i in range(index - 1):
                if tmp:
                    tmp = tmp.next
                else:
                    return
            if tmp:
                n = Node(val)
                temp = tmp.next
                tmp.next = n
                n.next = temp
        else:
            self.addAtHead(val)

    def deleteAtIndex(self, index: int) -> None:
        tmp = self.head
        if index != 0:
            for i in range(index - 1):
                if tmp:
                    tmp = tmp.next
            if tmp and tmp.next:
                tmp.next = tmp.next.next
        else:
            if tmp:
                self.head = tmp.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)