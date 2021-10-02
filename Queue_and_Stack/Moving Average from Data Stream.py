# _*_ coding: utf-8 _*_
"""
# @Time : 10/1/2021 8:21 PM
# @Author : byc
# @File : Moving Average from Data Stream.py
# @Description :
"""
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.w_size = size
        self.stream = deque([])
        self.s = 0

    def next(self, val: int) -> float:
        self.stream.append(val)
        self.s += val
        if len(self.stream) > self.w_size:
            self.s -= self.stream.popleft()
        return self.s / len(self.stream)

# class MovingAverage:
#
#     def __init__(self, size: int):
#         self.w_size = size
#         self.stream = [0] * size
#         self.head = 0
#         self.tail = -1
#
#     def next(self, val: int) -> float:
#         # Full
#
#         if self.head == 0:
#             if self.tail == self.w_size - 1:
#                 self.tail = 0
#                 self.head += 1
#             else:
#                 self.tail += 1
#         else:
#             if self.head == self.w_size - 1:
#                 self.tail += 1
#                 self.head = 0
#             else:
#                 self.tail += 1
#                 self.head += 1
#         self.stream[self.tail] = val
#         if self.head <= self.tail:
#             return sum(self.stream[self.head: self.tail + 1]) / (self.tail - self.head + 1)
#         else:
#             return mean(self.stream)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)