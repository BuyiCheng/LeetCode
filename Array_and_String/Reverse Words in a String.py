# _*_ coding: utf-8 _*_
"""
# @Time : 9/30/2021 8:58 PM
# @Author : byc
# @File : Reverse Words in a String.py
# @Description :
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.strip().split()
        s_list.reverse()
        return ' '.join(s_list)