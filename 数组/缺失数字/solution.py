# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，
找出 0 .. n 中没有出现在序列中的那个数。

输入: [3,0,1]
输出: 2

输入: [9,6,4,2,3,5,7,0,1]
输出: 8

说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        length = len(nums)
        max_index = length
        while i < length:
            if nums[i] == length:
                max_index = i
                i += 1
            elif nums[i] == i:
                i += 1
            else:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
        return max_index