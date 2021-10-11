# _*_ coding: utf-8 _*_
"""
# @Time : 10/11/2021 10:44 AM
# @Author : byc
# @File : Design HashMap.py
# @Description :
"""


class MyHashMap:

    def __init__(self):
        self.mod = 1001
        self.hashmap = dict()

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        if key in self.hashmap:
            return self.hashmap[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            self.hashmap.pop(key)