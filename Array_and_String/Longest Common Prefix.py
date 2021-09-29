# _*_ coding: utf-8 _*_
"""
# @Time : 9/29/2021 11:24 AM
# @Author : byc
# @File : Longest Common Prefix.py
# @Description :
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        len_list = [len(s) for s in strs]
        min_len = min(len_list)
        com_prefix = list()
        for i in range(min_len):
            c = strs[0][i]
            flag = True
            for s in strs:
                if s[i] == c:
                    continue
                else:
                    flag = False
                    break
            if flag:
                com_prefix.append(c)
            else:
                break

        return ''.join(com_prefix)