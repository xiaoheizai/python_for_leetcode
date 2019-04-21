# -*- coding: utf-8 -*-
"""
Created on Apr 21

@author: xiaoheizai
"""

'''
description:
给定一个整数数组，你需要寻找一个连续的子数组，
如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度。

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

说明 :
输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。
'''

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        temp_max = nums[0]
        temp_min = nums[-1]
        for t in range(len(nums)):
            if nums[t] < temp_max:
                j = t
            else:
                temp_max = nums[t]
        while t >= 0:
            if nums[t] > temp_min:
                i = t
            else:
                temp_min = nums[t]
            t -= 1
        if j == i:
            return 0
        else:
            return j - i + 1