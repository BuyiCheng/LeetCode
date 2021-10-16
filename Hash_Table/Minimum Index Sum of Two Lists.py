# _*_ coding: utf-8 _*_
"""
# @Time : 10/16/2021 2:58 PM
# @Author : byc
# @File : Minimum Index Sum of Two Lists.py
# @Description :
"""
from collections import defaultdict
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = defaultdict(list)

        for i in range(len(list1)):
            hashmap[list1[i]].append(i)
        for i in range(len(list2)):
            hashmap[list2[i]].append(i)
        hashmap_r = defaultdict(list)
        for k, v in hashmap.items():
            if len(v) == 2:
                hashmap_r[sum(v)].append(k)
        key = sorted(hashmap_r)[0]
        return hashmap_r[key]
