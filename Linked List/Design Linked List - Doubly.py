# _*_ coding: utf-8 _*_
"""
# @Time : 11/14/2021 9:54 AM
# @Author : byc
# @File : Design Linked List - Doubly.py
# @Description :
"""


class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


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
        n = DoublyNode(val)
        n.next = self.head
        if self.head:
            self.head.prev = n
        self.head = n

    def addAtTail(self, val: int) -> None:
        tmp = self.head
        n = DoublyNode(val)
        if tmp:
            while tmp.next:
                tmp = tmp.next
            tmp.next = n
            n.prev = tmp
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
                n = DoublyNode(val)
                temp = tmp.next
                tmp.next = n
                n.prev = tmp
                n.next = temp
                if temp:
                    temp.prev = n
        else:
            self.addAtHead(val)

    def deleteAtIndex(self, index: int) -> None:
        tmp = self.head
        if index != 0:
            for i in range(index - 1):
                if tmp:
                    tmp = tmp.next
            if tmp and tmp.next:
                next_e = tmp.next.next
                tmp.next = next_e
                if next_e:
                    next_e.prev = tmp
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