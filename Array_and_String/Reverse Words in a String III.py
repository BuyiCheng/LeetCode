# _*_ coding: utf-8 _*_
"""
# @Time : 9/30/2021 9:04 PM
# @Author : byc
# @File : Reverse Words in a String III.py
# @Description :
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w[::-1] for w in s.split()])