# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def dfs(self, index, nums, flags, path, res):
        length = len(nums)
        if index == length:
            res.append(path[:])
            return
        
        for i in range(length):
            if not flags[i]:
                if i > 0 and nums[i] == nums[i-1] and not flags[i-1]:
                    continue
                path.append(nums[i])
                flags[i] = True
                self.dfs(index+1, nums, flags, path, res)
                flags[i] = False
                path.pop()
            
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        flags = [False] * len(nums)
        result = []
        self.dfs(0, nums, flags, [], result)
        return result