# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def helper(param_list, param_i, param_j):
            while param_i < param_j:
                temp = param_list[param_i]
                param_list[param_i] = param_list[param_j]
                param_list[param_j] = temp
                param_i += 1
                param_j -= 1
                
        symbol = -1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                symbol = i + 1
        if symbol == -1:
            helper(nums, 0, len(nums)-1)
        else:
            k = -1
            for i in range(symbol, len(nums)):
                if nums[i] > nums[symbol-1]:
                    k = i
            temp = nums[symbol-1]
            nums[symbol-1] = nums[k]
            nums[k] = temp
            helper(nums, symbol, len(nums)-1)