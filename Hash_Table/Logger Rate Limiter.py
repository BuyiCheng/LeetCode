# _*_ coding: utf-8 _*_
"""
# @Time : 10/16/2021 3:02 PM
# @Author : byc
# @File : Logger Rate Limiter.py
# @Description :
"""


class Logger:

    def __init__(self):
        self.m = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.m:
            self.m[message] = timestamp + 10
        else:
            if timestamp < self.m[message]:
                return False
            self.m[message] = timestamp + 10
        return True
