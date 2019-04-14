# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

动态规划，a[i][j]表示到坐标（i,j）时路径数字和最小，a[m][n] = min(a[m-1][n], a[m][n-1]) + grid[m][n]
'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        a = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    a[i][j] = grid[i][j]
                elif i == 0:
                    a[i][j] = a[i][j-1] + grid[i][j]
                elif j == 0:
                    a[i][j] = a[i-1][j] + grid[i][j]
                else:
                    a[i][j] = min(a[i-1][j], a[i][j-1]) + grid[i][j]
        return a[m-1][n-1]