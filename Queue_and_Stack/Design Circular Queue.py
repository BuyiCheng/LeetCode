# _*_ coding: utf-8 _*_
"""
# @Time : 10/1/2021 5:45 PM
# @Author : byc
# @File : Design Circular Queue.py
# @Description :
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0] * k
        self.head = 0
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.head == self.tail:
            self.head, self.tail = 0, -1
        elif self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.tail == -1: return True
        return False

    def isFull(self) -> bool:
        if (self.head == 0 and self.tail == self.size - 1) or (self.tail + 1 == self.head and self.tail != -1):
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()