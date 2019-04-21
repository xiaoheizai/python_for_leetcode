# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，
数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 
你可以假定返回的数组不算在额外空间内。

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

思路：将对应数组下标的值置为负数，最后还是正数的数组下标+1就是缺失的值

'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        miss_list = []
        length = len(nums)
        for i in range(length):
            index = abs(nums[i]) - 1
            nums[index] = -1 * abs(nums[index])
        for i in range(length):
            if nums[i] > 0:
                miss_list.append(i+1)
        return miss_list