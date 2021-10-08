# _*_ coding: utf-8 _*_
"""
# @Time : 10/7/2021 8:44 PM
# @Author : byc
# @File : Implement Stack using Queues.py
# @Description :
"""


class MyStack:

    def __init__(self):
        self.queue = deque([])

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return True if len(self.queue) == 0 else False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()