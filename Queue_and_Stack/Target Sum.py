# _*_ coding: utf-8 _*_
"""
# @Time : 10/7/2021 8:02 PM
# @Author : byc
# @File : Target Sum.py
# @Description :
"""
from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[-nums[0]] += 1
        dp[nums[0]] += 1
        for i in nums[1:]:
            new_dp = defaultdict(int)
            for v in dp:
                new_dp[v + i] += dp[v]
                new_dp[v - i] += dp[v]
            dp = new_dp
        return dp[target]

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         if len(nums) ==1:
#             if nums[0] == target or nums[0] == -target:
#                 return 1
#             return 0
#         dp = list()
#         s = sum(nums)
#         if target > s or target < -s:
#             return 0
#         for _ in range(len(nums)):
#             dp.append([0]*(2*s+1))
#         dp[0][-nums[0]+s] += 1
#         dp[0][nums[0]+s] += 1
#         for i in range(1, len(nums)):
#             for j in range(-s, s+1):
#                 if j-nums[i] >= -s:
#                     dp[i][j+s] += dp[i-1][j-nums[i]+s]
#                 if j+nums[i] <= s:
#                     dp[i][j+s] += dp[i-1][j+nums[i]+s]
#         print(dp)
#         return dp[-1][target + s]