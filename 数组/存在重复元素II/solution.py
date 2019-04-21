# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 

输入: nums = [1,2,3,1], k = 3
输出: true

输入: nums = [1,0,1,1], k = 1
输出: true

输入: nums = [1,0,1,1], k = 1
输出: true
'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp_dict = {}
        i = 0
        length = len(nums)
        while i < length:
            try:
                temp_value = temp_dict[nums[i]]
                if i - temp_value <= k:
                    return True
                else:
                    temp_dict[nums[i]] = i
                    i += 1
            except KeyError:
                temp_dict[nums[i]] = i
                i += 1
        return False