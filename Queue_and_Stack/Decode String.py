# _*_ coding: utf-8 _*_
"""
# @Time : 10/7/2021 9:51 PM
# @Author : byc
# @File : Decode String.py
# @Description :
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        result = list()
        for c in s:
            if c == ']':
                sl = []
                while stack:
                    e = stack.pop()
                    if e == '[':
                        number = 0
                        nl = []
                        while stack:
                            if stack[-1].isalpha() or stack[-1] == '[': break
                            nl.append(stack.pop())
                        for i in range(len(nl)):
                            number += int(nl[i])*10**i
                        string = ''.join(sl[::-1])
                        stack.append(string*number)
                        break
                    else:
                        sl.append(e)
            else:
                stack.append(c)
            print(stack)
        return ''.join(stack)