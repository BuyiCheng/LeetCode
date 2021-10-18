# _*_ coding: utf-8 _*_
"""
# @Time : 10/18/2021 3:41 PM
# @Author : byc
# @File : Jewels and Stones.py
# @Description :
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count