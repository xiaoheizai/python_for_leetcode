# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 动态规划
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [i for i in range(n+1)]
        for i in range(n+1):
            j = 1
            while i - j * j >= 0:
                result[i] = min(result[i], result[i - j * j] + 1)
                j += 1
        return result[n]
		
# 广度优先搜索
from collections import deque
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        level = 0
        levels = deque([[n]])
        flags = [0 for _ in range(n+1)]
        while levels:
            node = levels.popleft()
            temp_list = []
            for value in node:
                flags[value] = 1
                j = 1
                temp = value - j * j
                while temp > 0:
                    j += 1
                    if flags[temp] == 0:
                        temp_list.append(temp)
                    temp = value - j * j
                if temp == 0:
                    temp_list = []
                    break
            if temp_list:
                levels.append(temp_list)    
            level += 1
        return level
