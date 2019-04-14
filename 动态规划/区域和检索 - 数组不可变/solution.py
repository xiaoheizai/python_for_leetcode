<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Apr 13

@author: xiaoheizai
"""

'''
description:
区域和检索 - 数组不可变:给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

说明:
你可以假设数组不可变。
会多次调用 sumRange 方法。

这道题主要考虑会多次调用sumRange方法，因而将结果保存下来，减少每次调用遍历的次数
动态规划：0到n的求和：f(n) = f(n-1) + s[n]
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        if len(self.nums) == 0:
            return None
        self.local_sum = [self.nums[0]]
        for i in range(1, len(self.nums)):
            self.local_sum.append(self.local_sum[i-1]+self.nums[i])

    def sumRange(self, i: int, j: int) -> int:
        if i > 0:
            temp_sum = self.local_sum[j] - self.local_sum[i-1]
        else:
            temp_sum = self.local_sum[j]
        return temp_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
=======
# -*- coding: utf-8 -*-
"""
Created on Apr 13

@author: xiaoheizai
"""

'''
description:
区域和检索 - 数组不可变:给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

说明:
你可以假设数组不可变。
会多次调用 sumRange 方法。

这道题主要考虑会多次调用sumRange方法，因而将结果保存下来，减少每次调用遍历的次数
动态规划：0到n的求和：f(n) = f(n-1) + s[n]
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        if len(self.nums) == 0:
            return None
        self.local_sum = [self.nums[0]]
        for i in range(1, len(self.nums)):
            self.local_sum.append(self.local_sum[i-1]+self.nums[i])

    def sumRange(self, i: int, j: int) -> int:
        if i > 0:
            temp_sum = self.local_sum[j] - self.local_sum[i-1]
        else:
            temp_sum = self.local_sum[j]
        return temp_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
>>>>>>> 动态规划题目
# param_1 = obj.sumRange(i,j)