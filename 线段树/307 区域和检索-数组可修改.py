# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。

示例:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
说明:

数组仅可以在 update 函数下进行修改。
你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-mutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lengths = len(nums)
        self.trees = [0] * (2 * self.lengths)
        j = self.lengths
        for value in nums:
            self.trees[j] = value
            j += 1
        j = self.lengths - 1
        while j > 0:
            self.trees[j] = self.trees[2 * j] + self.trees[2 * j + 1]
            j -= 1

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        new_index = i + self.lengths
        diff = self.trees[new_index] - val
        self.trees[new_index] = val
        j = new_index // 2
        while j > 0:
            self.trees[j] -= diff
            j = j // 2
            
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        result = 0
        new_i = self.lengths + i
        new_j = self.lengths +j
        while new_i <= new_j:
            if new_i % 2 == 1:
                result += self.trees[new_i]
                new_i += 1
            if new_j % 2 == 0:
                result += self.trees[new_j]
                new_j -= 1
            new_i = new_i // 2
            new_j = new_j // 2
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)