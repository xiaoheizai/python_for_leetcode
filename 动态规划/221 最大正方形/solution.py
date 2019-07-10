# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row == 0:
            return 0
        else:
            col = len(matrix[0])
            if col == 0:
                return 0
            else:
                length = 0
                a = [[0] * col for i in range(row)]
                for i in range(row):
                    for j in range(col):
                        if matrix[i][j] == "1":
                            if i == 0 or j == 0:
                                a[i][j] = 1
                            else:
                                a[i][j] = min(a[i-1][j], a[i-1][j-1], a[i][j-1]) + 1
                            length = max(length, a[i][j])
                return length**2