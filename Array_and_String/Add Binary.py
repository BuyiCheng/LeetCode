# _*_ coding: utf-8 _*_
"""
# @Time : 9/29/2021 10:59 AM
# @Author : byc
# @File : Add Binary.py
# @Description :
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        min_len = len(a) if len(a) <= len(b) else len(b)
        result = list()
        pre = 0
        for i in range(0, min_len):
            s = int(a[i]) + int(b[i]) + pre
            if s > 1:
                result.append(s % 2)
                pre = 1
            else:
                result.append(s)
                pre = 0
        for i in range(min_len, len(a)):
            if int(a[i])+pre > 1:
                result.append((int(a[i])+pre) % 2)
                pre = 1
            else:
                result.append(int(a[i])+pre)
                pre = 0
        for i in range(min_len, len(b)):
            if int(b[i])+pre > 1:
                result.append((int(b[i])+pre) % 2)
                pre = 1
            else:
                result.append(int(b[i])+pre)
                pre = 0
        if pre == 1:
            result.append(pre)
        return ''.join([str(e) for e in result[::-1]])