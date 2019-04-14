# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
例如，上图是一个7 x 3 的网格。有多少可能的路径？
说明：m 和 n 的值均不超过 100。

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

输入: m = 7, n = 3
输出: 28

动态规划    a[m][n] = a[m-1][n] + a[m][n-1]
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    a[i][j] = a[i-1][j] + a[i][j-1]
                elif i == 0:
                    a[i][j] = 1
                elif j == 0:
                    a[i][j] = 1
        return a[m-1][n-1]