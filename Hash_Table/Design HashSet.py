# _*_ coding: utf-8 _*_
"""
# @Time : 10/11/2021 10:43 AM
# @Author : byc
# @File : Design HashSet.py
# @Description :
"""


class MyHashSet:

    def __init__(self):
        self.mod = 1001
        self.hashset = [set()] * self.mod

    def add(self, key: int) -> None:
        hash_val = key % self.mod
        self.hashset[hash_val].add(key)

    def remove(self, key: int) -> None:
        hash_val = key % self.mod
        self.hashset[hash_val].discard(key)
        # if key in self.hashset[hash_val]:

    def contains(self, key: int) -> bool:
        hash_val = key % self.mod
        if key in self.hashset[hash_val]:
            return True
        return False
