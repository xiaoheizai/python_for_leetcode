# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution(object):
    def backtrack(self, index, nums, param_n, param_list):
        if index == param_n:
            param_list.append(nums[:])
        for i in range(index, param_n):
            nums[index], nums[i] = nums[i], nums[index]
            self.backtrack(index+1, nums, param_n, param_list)
            nums[i], nums[index] = nums[index], nums[i]
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        lens = len(nums)
        self.backtrack(0, nums, lens, result)
        return result