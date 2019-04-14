# -*- coding: utf-8 -*-
"""
Created on Apr 13

@author: xiaoheizai
"""

'''
description:
最大子序和:给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_result = float("-inf")
        temp_value = 0
        for number in nums:
            temp_value += number
            if temp_value > max_result:
                max_result = temp_value
            if temp_value < 0:
                temp_value = 0
        return max_result