# -*- coding: utf-8 -*-
"""
Created on Apr 20

@author: xiaoheizai
"""

'''
description:
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

动态规划：分为两步
1）计算第一间屋子到倒数第二间屋子的金额
2）计算第二间屋子到倒数第一间屋子的金额
取两者的最大
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        else:
            dp = [0] * (length - 1)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, length-1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
            dp_1 = [0] * (length - 1)
            dp_1[0] = nums[1]
            dp_1[1] = max(nums[1], nums[2])
            for i in range(2, length-1):
                dp_1[i] = max(dp_1[i-1], dp_1[i-2] + nums[i+1])
            return max(dp[-1], dp_1[-1])