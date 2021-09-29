# _*_ coding: utf-8 _*_
"""
# @Time : 9/28/2021 6:43 PM
# @Author : byc
# @File : Largest Number At Least Twice of Others.py
# @Description :
"""
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_e = max(nums)
        index = -1
        for i, e in enumerate(nums):
            if e == max_e:
                index = i
            elif max_e < 2 * e:
                index = -1
                break
        return index


if __name__ == '__main__':
    s = Solution()
    nums = [3,6,1,0]
    print(s.dominantIndex(nums))