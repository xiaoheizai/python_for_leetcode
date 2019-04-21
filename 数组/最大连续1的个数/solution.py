# -*- coding: utf-8 -*-
"""
Created on Apr 21

@author: xiaoheizai
"""

'''
description:
给定一个二进制数组， 计算其中最大连续1的个数。

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

注意：
输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。

'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        temp_count = 0
        for value in nums:
            if value == 1:
                temp_count += 1
            else:
                if temp_count > max_one:
                    max_one = temp_count
                temp_count = 0
        if temp_count > max_one:
            max_one = temp_count
            temp_count = 0
        return max_one