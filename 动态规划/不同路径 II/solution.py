# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

动态规划    a[m][n] = a[m-1][n] + a[m][n-1],其中a[m][n] = 0, 若该点没有办法走
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        a = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                        a[i][j] = 0
                else:
                    if i == 0 and j > 0:
                        if a[i][j-1] == 0:
                            a[i][j] = 0
                        else:
                            a[i][j] = 1
                    elif j == 0 and i > 0:
                        if a[i-1][j] == 0:
                            a[i][j] = 0
                        else:
                            a[i][j] = 1
                    elif i == 0 and j == 0:
                            a[i][j] = 1
                    else:
                        a[i][j] = a[i-1][j] + a[i][j-1]
                    
        return a[m-1][n-1]