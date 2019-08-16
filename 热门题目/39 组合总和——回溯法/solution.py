# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution(object):
    def helper(self, candidates, begin, end, path, res, target):
        if target == 0:
            res.append(path[:])
        
        for value in range(begin, end):
            temp = target - candidates[value]
            if temp < 0:
                break
            path.append(candidates[value])
            self.helper(candidates, value, end, path, res, temp)
            path.pop()
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        lens = len(candidates)
        candidates.sort()
        self.helper(candidates, 0, lens, path, res, target)
        return res