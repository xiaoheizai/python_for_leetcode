# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            result = [[1]]
            for i in range(1, numRows):
                temp = [1]
                for j in range(len(result[i-1])-1):
                    temp.append(result[i-1][j] + result[i-1][j+1])
                temp.append(1)
                result.append(temp)
            return result