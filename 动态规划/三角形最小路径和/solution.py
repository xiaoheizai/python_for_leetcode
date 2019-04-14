# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

动态规划，第n层第n个点的最小值为  s[n][j] = min(s[n-1][j-1], s[n-1][j]) + value[n][j], 注意边界的判断
          可以开辟一个临时空间保存每一层的最小值
   

'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        a = [triangle[0][0]]
        for i in range(1, len(triangle)):
            values = triangle[i]
            temp_list = []
            for j in range(len(values)):
                value = values[j]
                if j - 1 >= 0 and j < len(a):
                    current_value = min(a[j-1], a[j]) +  value
                elif j - 1 >= 0:
                    current_value = value + a[j-1]
                else:
                    current_value = value + a[j]
                temp_list.append(current_value)
            a = temp_list
        return min(a)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        a = triangle[-1].copy()
        length = len(triangle)
        j = length - 2
        while j >= 0:
            for i in range(len(triangle[j])):
                a[i] = min(a[i], a[i+1]) + triangle[j][i]
            j -= 1
        return a[0]