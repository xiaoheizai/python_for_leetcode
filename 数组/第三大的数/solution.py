# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
给定一个非空数组，返回此数组中第三大的数。
如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

输入: [3, 2, 1]
输出: 1
解释: 第三大的数是 1.

输入: [1, 2]
输出: 2
解释: 第三大的数不存在, 所以返回最大的数 2 .

'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        length = len(nums)
        a = [nums[0]]
        for i in range(1, length):
            if len(a) < 3:
                temp = True
                for value in a:
                    if value == nums[i]:
                        temp = False
                        break
                if temp:
                    a.append(nums[i])
                    a.sort(reverse=True)
            elif nums[i] > a[-1] and nums[i] != a[0] and nums[i] != a[1]:
                a[-1] = nums[i]
                a.sort(reverse=True)
        if len(a) == 3:
            return a[-1]
        elif len(a) < 3:
            return a[0]